from typing import Any, Callable, Dict, List, Optional, Union
from warnings import warn

from .contexts import Context
from .rich_responses import RichResponse, Text


class WebhookClient:
    """
    A client class for handling webhook requests from Dialogflow.

    This class allows to dinamically manipulate contexts and create responses
    to be sent back to Dialogflow (which will validate the response and send it
    back to the end-user).

    Parameters:
        request (dict): The webhook request object (``WebhookRequest``) from
            Dialogflow.

    Raises:
        TypeError: If the request is not a dictionary.

    See Also:
        For more information about the webhook request object, see the
        WebhookRequest_ section in Dialogflow's API reference.

    Attributes:
        query (str): The original query sent by the end-user.
        intent (str): The intent triggered by Dialogflow.
        action (str): The action defined for the intent.
        context (Context): An API class for handling input and output contexts.
        contexts (list(dict)): The array of input contexts.
        parameters (dict): The intent parameters extracted by Dialogflow.
        console_messages (list(RichResponse)): The response messages defined
            for the intent.
        original_request (str): The original request object from
            `detectIntent/query`.
        request_source (str): The source of the request.
        locale (str): The language code or locale of the original request.
        session (str): The session id of the conversation.

    .. _WebhookRequest: https://cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#webhookrequest
    """  # noqa: E501

    def __init__(self, request: Dict[str, Any]) -> None:
        if not isinstance(request, dict):
            raise TypeError('request argument must be a dictionary')

        self._response_messages: List[RichResponse] = []
        self._followup_event: Optional[Dict[str, Any]] = None

        self._process_request(request)

    def _process_request(self, request: Dict[str, Any]) -> None:
        """
        Set instance attributes from the webhook request.

        Parameters:
            request (dict): The webhook request object from Dialogflow.
        """
        query_result = request['queryResult']

        self.intent = query_result['intent']['displayName']
        self.action = query_result.get('action')
        self.parameters = query_result.get('parameters', {})
        self.contexts = query_result.get('outputContexts', [])
        self.original_request = request.get('originalDetectIntentRequest', {})
        self.request_source = self.original_request.get('source')
        self.query = query_result['queryText']
        self.locale = query_result['languageCode']
        self.session = request['session']
        self.context = Context(self.contexts, self.session)
        self.console_messages = self._process_console_messages(request)

    @property
    def followup_event(self) -> Optional[Dict[str, Any]]:
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

        Raises:
            TypeError: If the event is not a string or a dictionary.
        """  # noqa: D401, E501
        return self._followup_event

    @followup_event.setter
    def followup_event(self, event: Union[str, Dict[str, Any]]) -> None:
        if isinstance(event, str):
            event = {'name': event}

        if not isinstance(event, dict):
            raise TypeError('event argument must be a string or a dictionary')

        event['languageCode'] = event.get('languageCode', self.locale)

        self._followup_event = event

    @classmethod
    def _process_console_messages(
        cls,
        request: Dict[str, Any]
    ) -> List[RichResponse]:
        """Get messages defined in Dialogflow's console for matched intent."""
        fulfillment_messages = request['queryResult'].get(
            'fulfillmentMessages',
            []
        )

        return [RichResponse._from_dict(message)
                for message in fulfillment_messages]

    def add(
        self,
        responses: Union[str, RichResponse, List[Union[str, RichResponse]]]
    ) -> None:
        """
        Add response messages to be sent back to Dialogflow.

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
            responses (str, RichResponse, list(str, RichResponse)):
                A single response message or a list of response messages.
        """  # noqa: E501
        if not isinstance(responses, list):
            responses = [responses]

        for response in responses:
            self._add_response(response)

    def _add_response(self, response: Union[str, RichResponse]) -> None:
        """Add a single response to be sent back to Dialogflow."""
        if isinstance(response, str):
            response = Text(response)

        if not isinstance(response, RichResponse):
            raise TypeError(
                'response argument must be a string or a RichResponse'
            )

        self._response_messages.append(response)

    def set_followup_event(self, event: Union[str, Dict[str, Any]]) -> None:
        """
        Set the followup event to be triggered by Dialogflow.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`followup_event` attribute instead.

        Parameters:
            event (str, dict): The event to be triggered by Dialogflow.

        Warns:
            DeprecationWarning: Assign value to the :attr:`followup_event`
                attribute instead.
        """
        warn(
            'set_followup_event() is deprecated; '
            'assign value to the followup_event attribute instead',
            DeprecationWarning
        )

        self.followup_event = event

    def handle_request(
        self,
        handler: Union[
            Callable[['WebhookClient'], Optional[Any]],
            Dict[str, Callable[['WebhookClient'], Optional[Any]]]
        ]
    ) -> Optional[Any]:
        """
        Handle the webhook request using a handler or a mapping of handlers.

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
                ...
                >>> def fallback_handler(agent):
                ...     agent.add('Sorry, I missed what you said.')
                ...     agent.add('Can you say that again?')
                ...
                >>> handler = {
                ...     'Default Welcome Intent': welcome_handler,
                ...     'Default Fallback Intent': fallback_handler,
                ... }

        Parameters:
            handler (callable, dict(str, callable)): The handler function or
                a mapping of intents to handler functions.

        Raises:
            TypeError: If the handler is not a function or a map of functions.

        Returns:
            any, optional: The output from the handler function (if any).
        """  # noqa: E501
        if isinstance(handler, dict):
            handler_function = handler.get(self.intent)
        else:
            handler_function = handler

        if not callable(handler_function):
            raise TypeError(
                'handler argument must be a function or a map of functions'
            )

        return handler_function(self)

    @property
    def _response_messages_as_dicts(self) -> List[Dict[str, Any]]:
        """list of dict: The list of response messages."""  # noqa: D403
        return [response._as_dict() for response in self._response_messages]

    @property
    def response(self) -> Dict[str, Any]:
        """
        dict: The generated webhook response object (``WebhookResponse``).

        See Also:
            For more information about the webhook response object, see the
            WebhookResponse_ section in Dialogflow's API reference.

        .. _WebhookResponse: https://cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#webhookresponse
        """  # noqa: D401, E501
        response = {}

        if self._response_messages:
            response['fulfillmentMessages'] = self._response_messages_as_dicts

        if self.followup_event is not None:
            response['followupEventInput'] = self.followup_event

        if self.context.contexts:
            response['outputContexts'] = self.context\
                .get_output_contexts_array()

        if self.request_source is not None:
            response['source'] = self.request_source

        return response
