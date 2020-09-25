import pytest

from dialogflow_fulfillment import WebhookClient


def test_webhook_client_non_dict():
    with pytest.raises(TypeError):
        WebhookClient('this is not a dict')


def test_webhook_client_add_text(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        agent.add('this is a text')

    agent.handle_request(handler)

    assert agent.response['fulfillmentMessages'] == [
        {'text': {'text': ['this is a text']}}
    ]


def test_webhook_client_add_list_of_texts(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        agent.add(['this', 'is', 'a', 'list', 'of', 'texts'])

    agent.handle_request(handler)

    assert agent.response['fulfillmentMessages'] == [
        {'text': {'text': ['this']}},
        {'text': {'text': ['is']}},
        {'text': {'text': ['a']}},
        {'text': {'text': ['list']}},
        {'text': {'text': ['of']}},
        {'text': {'text': ['texts']}}
    ]


def test_webhook_client_add_non_richresponse(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        agent.add({'this': 'is not a RichResponse'})

    with pytest.raises(TypeError):
        agent.handle_request(handler)


def test_webhook_client_set_followup_event(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        with pytest.warns(DeprecationWarning):
            agent.set_followup_event('test_event')

    agent.handle_request(handler)

    assert agent.response['followupEventInput'] == {
        'name': 'test_event',
        'languageCode': webhook_request['queryResult']['languageCode']
    }


def test_webhook_client_set_followup_event_by_dict(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        with pytest.warns(DeprecationWarning):
            agent.set_followup_event({'name': 'test_event'})

    agent.handle_request(handler)

    assert agent.response['followupEventInput'] == {
        'name': 'test_event',
        'languageCode': webhook_request['queryResult']['languageCode']
    }


def test_webhook_client_assign_followup_event(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        agent.followup_event = 'test_event'

    agent.handle_request(handler)

    assert agent.response['followupEventInput'] == {
        'name': 'test_event',
        'languageCode': webhook_request['queryResult']['languageCode']
    }


def test_webhook_client_assign_followup_event_by_dict(webhook_request):
    agent = WebhookClient(webhook_request)

    def handler(agent):
        agent.followup_event = {'name': 'test_event'}

    agent.handle_request(handler)

    assert agent.response['followupEventInput'] == {
        'name': 'test_event',
        'languageCode': webhook_request['queryResult']['languageCode']
    }


def test_webhook_client_handler_intent_map(webhook_request):
    agent = WebhookClient(webhook_request)

    handler = {
        'Default Welcome Intent': lambda agent: agent.add('Hello!'),
        'Default Fallback Intent': lambda agent: agent.add('What was that?'),
    }

    agent.handle_request(handler)

    assert agent.response['fulfillmentMessages'] == [
        {'text': {'text': ['Hello!']}}
    ]


def test_webhook_client_non_callable_handler(webhook_request):
    agent = WebhookClient(webhook_request)

    handler = 'this is not a callable'

    with pytest.raises(TypeError):
        agent.handle_request(handler)


def test_webhook_client_no_contexts(webhook_request):
    modified_webhook_request = webhook_request
    modified_webhook_request['queryResult']['outputContexts'] = []

    agent = WebhookClient(modified_webhook_request)

    def handler(agent):
        pass

    agent.handle_request(handler)

    assert 'outputContexts' not in agent.response


def test_webhook_client_with_request_source(webhook_request):
    modified_webhook_request = webhook_request
    modified_webhook_request['originalDetectIntentRequest']['source'] = \
        'PLATFORM_UNSPECIFIED'

    agent = WebhookClient(modified_webhook_request)

    def handler(agent):
        pass

    agent.handle_request(handler)

    assert agent.response['source'] == 'PLATFORM_UNSPECIFIED'


def test_webhook_client_with_unknown_message(webhook_request):
    modified_webhook_request = webhook_request
    modified_webhook_request['queryResult']['fulfillmentMessages'] = [
        {
            'foo': {
                'foo': ['bar']
            }
        }
    ]

    with pytest.raises(TypeError):
        WebhookClient(modified_webhook_request)


def test_webhook_client_set_followup_event_non_string_or_dict(webhook_request):
    agent = WebhookClient(webhook_request)

    with pytest.raises(TypeError):
        agent.followup_event = ['this', 'is', 'not', 'an', 'event']
