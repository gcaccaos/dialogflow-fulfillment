from uuid import uuid4

import pytest


@pytest.fixture()
def session():
    return str(uuid4())


@pytest.fixture()
def response_id():
    return str(uuid4())


@pytest.fixture()
def intent_id():
    return str(uuid4())


@pytest.fixture()
def text():
    return 'this is a text'


@pytest.fixture()
def quick_replies():
    return ['reply 1', 'reply 2', 'reply 3']


@pytest.fixture()
def payload():
    return {'test key 1': 'test value 1', 'test key 2': 'test value 2'}


@pytest.fixture()
def image_url():
    return 'https://test.url/image.jpg'


@pytest.fixture()
def title():
    return 'this is a title'


@pytest.fixture()
def subtitle():
    return 'this is a subtitle'


@pytest.fixture()
def buttons():
    return [
        {'text': 'text 1', 'postback': 'postback 1'},
        {'text': 'text 2', 'postback': 'postback 2'},
        {'text': 'text 3', 'postback': 'postback 3'}
    ]


@pytest.fixture()
def webhook_request(
    response_id,
    session,
    intent_id,
    text,
    title,
    subtitle,
    image_url,
    buttons,
    payload,
    quick_replies
):
    project_id = 'PROJECT_ID'

    return {
        'responseId': response_id,
        'queryResult': {
            'queryText': 'Hi',
            'parameters': {},
            'allRequiredParamsPresent': True,
            'fulfillmentText': 'Hello! How can I help you?',
            'fulfillmentMessages': [
                {'text': {'text': [text]}},
                {'image': {'imageUri': image_url}},
                {
                    'card': {
                        'title': title,
                        'subtitle': subtitle,
                        'imageUri': image_url,
                        'buttons': buttons
                    }
                },
                {'payload': payload},
                {'quickReplies': {'quickReplies': quick_replies}}
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
