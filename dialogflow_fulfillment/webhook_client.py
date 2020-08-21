from typing import Any, Callable, Dict, List, Optional, Union
from warnings import warn

from .contexts import Context
from .rich_responses import (Card, Image, Payload, QuickReplies, RichResponse,
                             Text)


class WebhookClient:
    """
    A client class for handling webhook requests from Dialogflow.

    This class allows to dinamically manipulate contexts and create responses
    to be sent back to Dialogflow (which will validate the response and send it
    back to the end-user).

    Parameters:
        request (dict): The webhook request object (:obj:`WebhookRequest`) from
            Dialogflow.

    Raises:
        TypeError: If the request is not a dictionary.

    See also:
        For more information about the webhook request object, see the
        WebhookRequest_ section in Dialogflow's API reference.

    Attributes:
        query (str): The original query sent by the end-user.
        intent (str): The intent triggered by Dialogflow.
        action (str): The action defined for the intent.
        context (:class:`.Context`): An API class for handling input and output
            contexts.
        contexts (list(dict)): The array of input contexts.
        parameters (dict): The intent parameters extracted by Dialogflow.
        console_messages (list of :class:`.RichResponse`): The response
            messages defined for the intent.
        original_request (str): The original request object from
            `detectIntent/query`.
        request_source (str): The source of the request.
        locale (str): The language code or locale of the original request.
        session (str): The session id of the conversation.

    .. _WebhookRequest: https://cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#webhookrequest
    """

    def __init__(self, request: Dict) -> None:
        if not isinstance(request, dict):
            raise TypeError('request argument must be a dictionary')

        self._request = request
        self._response = {}
        self._response_messages = []
        self._followup_event = None

        self._process_request()

    def _process_request(self) -> None:
        """
        Processes a Dialogflow's fulfillment webhook request and sets instance
        variables
        """
        self.intent = self._request['queryResult']['intent']['displayName']
        self.action = self._request['queryResult'].get('action')
        self.parameters = self._request['queryResult'].get('parameters', {})
        self.contexts = self._request['queryResult'].get('outputContexts', [])
        self.original_request = self._request['originalDetectIntentRequest']
        self.request_source = self._request['originalDetectIntentRequest'].get('source')
        self.query = self._request['queryResult']['queryText']
        self.locale = self._request['queryResult']['languageCode']
        self.session = self._request['session']
        self.context = Context(self.contexts, self.session)
        self.console_messages = self._get_console_messages()

    @property
    def followup_event(self) -> Optional[Dict]:
        """
        dict, optional: The followup event to be triggered by the response.

        Examples:
            Accessing the :attr:`followup_event` attribute:

                >>> agent.followup_event
                None

            Assigning an event name to the :attr:`followup_event` attribute:

                >>> agent.followup_event = 'WELCOME'
                >>> agent.followup_event
                {'name': 'WELCOME', 'languageCode': 'en-US'}

            Assigning an event dictionary to the :attr:`followup_event`
            attribute:

                >>> agent.followup_event = {'name': 'GOODBYE', 'languageCode': 'en-US'}
                >>> agent.followup_event
                {'name': 'GOODBYE', 'languageCode': 'en-US'}
        """
        return self._followup_event

    @followup_event.setter
    def followup_event(self, event: Union[str, Dict]) -> None:
        if isinstance(event, str):
            event = {'name': event}

        event['languageCode'] = event.get('languageCode', self.locale)

        self._followup_event = event

    def _get_console_messages(self) -> List[RichResponse]:
        """Get messages defined in Dialogflow's console for matched intent"""
        return [self._convert_message_dictionary(message) for message
                in self._request['queryResult'].get('fulfillmentMessages', [])]

    def _convert_message_dictionary(self, message) -> None:
        """Converts message dictionary to RichResponse"""
        if 'text' in message:
            return Text._from_dict(message)
        elif 'image' in message:
            return Image._from_dict(message)
        elif 'card' in message:
            return Card._from_dict(message)
        elif 'quickReplies' in message:
            return QuickReplies._from_dict(message)
        elif 'payload' in message:
            return Payload._from_dict(message)

        raise TypeError('unsupported message type')

    def add(
        self,
        responses: Union[str, RichResponse, List[Union[str, RichResponse]]]
    ) -> None:
        """
        Adds response messages to be sent back to Dialogflow (which will send
        the messages to the end-user).

        Examples:
            Adding a simple text response as a string:

                >>> agent.add('Hi! How can I help you?')

            Adding multiple rich responses one at a time:

                >>> agent.add(Text('How are you feeling today?'))
                >>> agent.add(QuickReplies(quick_replies=['Happy :)', 'Sad :(']))

            Adding multiple rich responses at once:

                >>> responses = [
                ...     Text('How are you feeling today?'),
                ...     QuickReplies(quick_replies=['Happy :)', 'Sad :('])
                ... ]
                >>> agent.add(responses)

        Parameters:
            responses (str, RichResponse or list of str or RichResponse):
                A single response message or a list of response messages.
        """
        if not isinstance(responses, list):
            responses = [responses]

        for response in responses:
            self._add_response(response)

    def _add_response(self, response) -> None:
        """Adds a response to be sent"""
        if isinstance(response, str):
            response = Text(response)

        if not isinstance(response, RichResponse):
            raise TypeError('response argument must be a string or a RichResponse')

        self._response_messages.append(response)

    def set_followup_event(self, event: Union[str, Dict]) -> None:
        """
        Sets the followup event to be triggered by Dialogflow.

        Warning:
            This method is deprecated and will be removed. Assign event (string
            or dictionary) to the :attr:`followup_event` attribute instead.

        Parameters:
            event (str or dict): The event to be triggered by Dialogflow.

        Warns:
            DeprecationWarning: Assign event to the :attr:`followup_event`
                attribute instead.
        """
        warn('set_followup_event() is deprecated; assign event to the followup_event attribute instead',
             DeprecationWarning)

        self.followup_event = event

    def handle_request(
        self,
        handler: Union[
            Callable[['WebhookClient'], Optional[Any]],
            Dict[str, Callable[['WebhookClient'], Optional[Any]]]
        ]
    ) -> Optional[Any]:
        """
        Handles the webhook request using a handler function or a mapping of
        intents to handler functions and returns the handler's output (if any).

        Parameters:
            handler (callable or dict(str, callable)): The handler function or
                a mapping of intents to handler functions.

        Raises:
            TypeError: `handler` argument must be a function or a map of
                functions

        Returns:
            any, optional: The output from the handler function (if any).
        """
        handler_function = handler.get(self.intent) if isinstance(handler, dict) else handler

        if not callable(handler_function):
            raise TypeError('handler argument must be a function or a map of functions')

        result = handler_function(self)

        self._send_responses()

        return result

    def _send_responses(self) -> None:
        """Adds and sends response to Dialogflow fulfillment webhook request"""
        if self._response_messages:
            self._response['fulfillmentMessages'] = self._build_response_messages()

        if self.followup_event is not None:
            self._response['followupEventInput'] = self.followup_event

        if self.contexts:
            self._response['outputContexts'] = self.context.get_output_contexts_array()

        if self.request_source is not None:
            self._response['source'] = self.request_source

    def _build_response_messages(self) -> List[Dict]:
        """Builds a list of message objects to send back to Dialogflow"""
        return [response._as_dict() for response in self._response_messages]

    @property
    def response(self) -> Dict:
        """
        dict: The generated response object (WebhookResponse).
        """
        return self._response
