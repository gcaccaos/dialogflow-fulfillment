"""Dialogflow's Webhook Client class module"""
from .contexts import Context
from .rich_responses import QuickReplies, RichResponse, Text


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
        console_messages = self._request.get('queryResult').get('fulfillmentMessages', [])

        for index, message in enumerate(console_messages):
            if 'text' in message:
                console_messages[index] = Text(*message.get('text'))

            elif 'quickReplies' in message:
                console_messages[index] = QuickReplies(*message.get('quickReplies'))

        return console_messages

    def add(self, responses):
        """Adds a RichResponse or a list of RichResponse messages"""
        if isinstance(responses, str):
            responses = Text(responses)

        if not isinstance(responses, list):
            responses = [responses]

        responses = filter(lambda response: isinstance(response, RichResponse),
                           responses)

        self._response_messages.extend(responses)

    def set_followup_event(self, event):
        """Sets the followup event"""
        if isinstance(event, str):
            event = {'name': event}

        if 'languageCode' not in event:
            event['languageCode'] = self.locale

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
