from uuid import uuid4

import pytest

from dialogflow_fulfillment import WebhookClient


@pytest.fixture()
def webhook_request():
    response_id = str(uuid4())
    session = str(uuid4())
    project_id = 'PROJECT_ID'
    intent_id = str(uuid4())

    return {
        'responseId': response_id,
        'queryResult': {
            'queryText': 'Hi',
            'parameters': {},
            'allRequiredParamsPresent': True,
            'fulfillmentText': 'Hello! How can I help you?',
            'fulfillmentMessages': [
                {
                    'text': {
                        'text': [
                            'Hello! How can I help you?'
                        ]
                    }
                },
                {
                    'image': {
                        'imageUri': 'https://image.url/image.jpg'
                    }
                },
                {
                    'card': {
                        'title': 'test title',
                        'subtitle': 'test subtitle',
                        'imageUri': 'https://image.url/image.jpg',
                        'buttons': [
                            {
                                'text': 'this is a text',
                                'postback': 'this is a postback text'
                            },
                            {
                                'text': 'this is a text 2',
                                'postback': 'this is a postback text 2'
                            },
                            {
                                'text': 'this is a text 3',
                                'postback': 'this is a postback text 3'
                            }
                        ]
                    }
                },
                {
                    'payload': {
                        'test key 1': 'test value 1',
                        'test key 2': 'test value 2'
                    }
                },
                {
                    'quickReplies': {
                        'quickReplies': [
                            'quick reply 1',
                            'quick reply 2',
                            'quick reply 3'
                        ]
                    }
                }
            ],
            'outputContexts': [
                {
                    'name': f'projects/{project_id}/agent/sessions/{session}/contexts/__system_counters__',  # noqa: E501
                    'parameters': {
                        'no-input': 0,
                        'no-match': 0
                    }
                }
            ],
            'intent': {
                'name': f'projects/{project_id}/agent/intents/{intent_id}',
                'displayName': 'Default Welcome Intent'
            },
            'intentDetectionConfidence': 1,
            'languageCode': 'en'
        },
        'originalDetectIntentRequest': {
            'payload': {},
        },
        'session': f'projects/{project_id}/agent/sessions/{session}'
    }


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
