"""Dialogflow's Webhook Client class module"""
from .contexts import Context
from .rich_responses import Payload, QuickReplies, RichResponse, Text


class WebhookClient: # pylint: disable=too-many-instance-attributes
    """Class for handling Dialogflow's fulfillment webhook API v2 requests"""

    def __init__(self, request):
        self._request = request
        self._response = {}
        self._response_messages = []
        self._followup_event = None

        self._process_request()

    def _process_request(self):
        """
        Processes a Dialogflow's fulfillment webhook request and sets instance
        variables
        """
        self.intent = self._request.get('queryResult').get('intent').get('displayName')
        self.action = self._request.get('queryResult').get('action')
        self.parameters = self._request.get('queryResult').get('parameters', {})
        self.contexts = self._request.get('queryResult').get('outputContexts', [])
        self.original_request = self._request.get('originalDetectIntentRequest')
        self.request_source = self.original_request.get('source')
        self.query = self._request.get('queryResult').get('queryText')
        self.locale = self._request.get('queryResult').get('languageCode')
        self.session = self._request.get('session')
        self.context = Context(self.contexts, self.session)
        self.console_messages = self._get_console_messages()
        self.alternative_query_results = self._request.get('alternativeQueryResults')

    def _get_console_messages(self):
        """Get messages defined in Dialogflow's console for matched intent"""
        console_messages = []

        for message in self._request.get('queryResult').get('fulfillmentMessages', []):
            message = self._convert_message_dictionary(message)
            console_messages.append(message)

        return console_messages

    def _convert_message_dictionary(self, message):
        """Converts message dictionary to RichResponse"""
        if 'text' in message:
            return Text(message.get('text').get('text')[0])
        elif 'quickReplies' in message:
            return QuickReplies(message.get('quickReplies').get('quickReplies'))
        elif 'payload' in message:
            return Payload(message.get('payload'))
        else:
            raise TypeError('unsupported message type')

    def add(self, responses):
        """Adds a response or list of messages"""
        if not isinstance(responses, list):
            responses = [responses]

        for response in responses:
            self._add_response(response)

    def _add_response(self, response):
        """Adds a response to be sent"""
        if isinstance(response, str):
            response = Text(response)
        elif isinstance(response, dict):
            response = self._convert_message(response)

        if not isinstance(response, RichResponse):
            raise TypeError('response argument must be a RichResponse')

        self._response_messages.append(response)

    def set_followup_event(self, event):
        """Sets the followup event"""
        if isinstance(event, str):
            event = {'name': event}

        event['languageCode'] = event.get('languageCode', self.locale)

        self._followup_event = event

    def handle_request(self, handler):
        """Handles the request using a handler or map of handlers"""
        if callable(handler):
            result = handler(self)
        elif isinstance(handler, dict):
            result = handler.get(self.intent)(self)
        else:
            raise TypeError('handler argument must be a function or a map of functions')

        self._send_responses()

        return result

    def _send_responses(self):
        """Adds and sends response to Dialogflow fulfillment webhook request"""
        if self._response_messages:
            self._response['fulfillmentMessages'] = self._build_response_messages()

        if self._followup_event is not None:
            self._response['followupEventInput'] = self._followup_event

        if self.contexts:
            self._response['outputContexts'] = self.context.get_output_contexts_array()

        if self.request_source is not None:
            self._response['source'] = self.request_source

    def _build_response_messages(self):
        """Builds a list of message objects to send back to Dialogflow"""
        return list(map(lambda response: response._get_response_object(), # pylint: disable=protected-access
                        self._response_messages))

    @property
    def response(self):
        """Returns the Dialogflow's fulfillment webhook response"""
        return self._response
