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

        self._response_messages = []
        self._followup_event = None

        self._process_request(request)

    def _process_request(self, request) -> None:
        """
        Processes a Dialogflow's fulfillment webhook request and sets instance
        variables
        """
        self.intent = request['queryResult']['intent']['displayName']
        self.action = request['queryResult'].get('action')
        self.parameters = request['queryResult'].get('parameters', {})
        self.contexts = request['queryResult'].get('outputContexts', [])
        self.original_request = request['originalDetectIntentRequest']
        self.request_source = request['originalDetectIntentRequest']\
            .get('source')
        self.query = request['queryResult']['queryText']
        self.locale = request['queryResult']['languageCode']
        self.session = request['session']
        self.context = Context(self.contexts, self.session)
        self.console_messages = self._process_console_messages(request)

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

    def _process_console_messages(self, request) -> List[RichResponse]:
        """Get messages defined in Dialogflow's console for matched intent"""
        fulfillment_messages = request['queryResult']\
            .get('fulfillmentMessages', [])

        return [self._convert_message_dictionary(message)
                for message in fulfillment_messages]

    def _convert_message_dictionary(self, message) -> None:
        """Converts message dictionary to RichResponse"""
        # TODO: refactor to reduce the cyclomatic complexity (use dict instead)
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
            This method is deprecated and will be removed. Assign value to the
            :attr:`followup_event` attribute instead.

        Parameters:
            event (str or dict): The event to be triggered by Dialogflow.

        Warns:
            DeprecationWarning: Assign value to the :attr:`followup_event`
                attribute instead.
        """
        warn('set_followup_event() is deprecated; assign value to the followup_event attribute instead',
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

        In order to manipulate the conversation programatically, the handler
        function must receive an instance of :class:`WebhookClient` as a
        parameter. Then, inside the function, :class:`WebhookClient`'s
        attributes and methods can be used to access and manipulate the webhook
        request attributes and generate the webhook response.

        Alternatively, this method can receive a mapping of handler functions
        for each intent.

        Note:
            If a mapping of handler functions is provided, the name of the
            corresponding intent must be written exactly as it is in
            Dialogflow.

        Finally, once the request has been handled, the generated webhook
        response can be accessed via the :attr:`response` attribute.

        Examples:
            Creating a simple handler function that sends a text and a
            collection of quick reply buttons to the end-user (the response is
            independent of the triggered intent):

                >>> def handler(agent: WebhookClient) -> None:
                ...     agent.add('How are you feeling today?')
                ...     agent.add(QuickReplies(quick_replies=['Happy :)', 'Sad :(']))

            Creating a mapping of handler functions for different intents:

                >>> def welcome_handler(agent):
                ...     agent.add('Hi!')
                ...     agent.add('How can I help you?')
                >>> def fallback_handler(agent):
                ...     agent.add('Sorry, I missed what you said.')
                ...     agent.add('Can you say that again?')
                >>> handler = {
                ...     'Default Welcome Intent': welcome_handler,
                ...     'Default Fallback Intent': fallback_handler,
                ... }

        Parameters:
            handler (callable or dict(str, callable)): The handler function or
                a mapping of intents to handler functions.

        Raises:
            TypeError: If the handler is not a function or a map of functions.

        Returns:
            any, optional: The output from the handler function (if any).
        """
        handler_function = handler.get(self.intent) if isinstance(handler, dict) else handler

        if not callable(handler_function):
            raise TypeError('handler argument must be a function or a map of functions')

        return handler_function(self)

    def _build_response_messages(self) -> List[Dict]:
        """
        Converts the RichResponse messages to dictionaries before sending them
        back to Dialogflow.

        Returns:
            list of dict: The list of outgoing response message objects.
        """
        return [response._as_dict() for response in self._response_messages]

    @property
    def response(self) -> Dict:
        """
        dict: The generated webhook response object (:obj:`WebhookResponse`).

        See also:
            For more information about the webhook response object, see the
            WebhookResponse_ section in Dialogflow's API reference.

        .. _WebhookResponse: https://cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#webhookresponse
        """
        response = {}

        if self._response_messages:
            response.update({'fulfillmentMessages': self._build_response_messages()})

        if self.followup_event is not None:
            response.update({'followupEventInput': self.followup_event})

        if self.contexts:
            response.update({'outputContexts': self.context.get_output_contexts_array()})

        if self.request_source is not None:
            response.update({'source': self.request_source})

        return response
