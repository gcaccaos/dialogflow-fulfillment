from typing import Any, Callable, Dict, List, Optional, Union

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
        request (dict): The request object (WebhookRequest) from Dialogflow.

    Attributes:
        query (str): The original query sent by the end-user.
        intent (str): The intent triggered by Dialogflow.
        action (str): The action defined for the intent.
        context (:class:`.Context`): An API class for handling input and output
            contexts.
        contexts (list(dict)): The array of input contexts.
        parameters (dict): The intent parameters extracted by Dialogflow.
        console_messages (list(:class:`.RichResponse`)): The response messages
            defined for the intent.
        original_request (str): The original request object from
            `detectIntent/query`.
        request_source (str): The source of the request.
        locale (str): The language code or locale for the original request.
        session (str): The session of the conversation.

    Raises:
        TypeError: `request` argument must be a dictionary
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

    def _get_console_messages(self) -> List[RichResponse]:
        """Get messages defined in Dialogflow's console for matched intent"""
        console_messages = []

        for message in self._request['queryResult'].get('fulfillmentMessages', []):
            message = self._convert_message_dictionary(message)
            console_messages.append(message)

        return console_messages

    def _convert_message_dictionary(self, message) -> None:
        """Converts message dictionary to RichResponse"""
        if 'text' in message:
            return Text(message['text'].get('text', [])[0])
        elif 'image' in message:
            return Image(message['image'].get('imageUri', ''))
        elif 'card' in message:
            return Card(
                title=message['card'].get('title'),
                subtitle=message['card'].get('subtitle'),
                image_url=message['card'].get('imageUri'),
                buttons=message['card'].get('buttons'),
            )
        elif 'quickReplies' in message:
            return QuickReplies(
                title=message['quickReplies'].get('title'),
                quick_replies=message['quickReplies'].get('quickReplies')
            )
        elif 'payload' in message:
            return Payload(message['payload'])

        raise TypeError('unsupported message type')

    def add(
        self,
        responses: Union[str, RichResponse, List[Union[str, RichResponse]]]
    ) -> None:
        """
        Adds response messages to be sent back to Dialogflow (which will send
        the messages to the end-user).

        Parameters:
            responses (str, RichResponse or list(str or RichResponse)):
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

        Parameters:
            event (str or dict): The event to be triggered by Dialogflow.
        """
        if isinstance(event, str):
            event = {'name': event}

        event['languageCode'] = event.get('languageCode', self.locale)

        self._followup_event = event

    def handle_request(
        self,
        handler: Union[Callable, Dict[str, Callable]]
    ) -> Optional[Any]:
        """
        Handles the webhook request using a handler function or a mapping of
        intents to handler functions and returns the handler's output (if any).

        Parameters:
            handler (callable or dict(str, callable)): The handler function or
                a mapping of intents to handler functions.

        Returns:
            any, optional: The output from the handler function (if any).

        Raises:
            TypeError: `handler` argument must be a function or a map of
                functions
        """
        if callable(handler):
            result = handler(self)
        elif isinstance(handler, dict):
            result = handler.get(self.intent)(self)
        else:
            raise TypeError('handler argument must be a function or a map of functions')

        self._send_responses()

        return result

    def _send_responses(self) -> None:
        """Adds and sends response to Dialogflow fulfillment webhook request"""
        if self._response_messages:
            self._response['fulfillmentMessages'] = self._build_response_messages()

        if self._followup_event is not None:
            self._response['followupEventInput'] = self._followup_event

        if self.contexts:
            self._response['outputContexts'] = self.context.get_output_contexts_array()

        if self.request_source is not None:
            self._response['source'] = self.request_source

    def _build_response_messages(self) -> List[Dict]:
        """Builds a list of message objects to send back to Dialogflow"""
        return list(map(lambda response: response._get_response_object(),
                        self._response_messages))

    @property
    def response(self) -> Dict:
        """
        Returns the generated response object (WebhookResponse) to be sent back
        to Dialogflow.

        Returns:
            dict: The generated response object (WebhookResponse).
        """
        return self._response
