from uuid import uuid4

import pytest


@pytest.fixture()
def session():
    """Generate a random session ID (UUID4)."""
    return str(uuid4())


@pytest.fixture()
def response_id():
    """Generate a random response ID (UUID4)."""
    return str(uuid4())


@pytest.fixture()
def intent_id():
    """Generate a random intent ID (UUID4)."""
    return str(uuid4())


@pytest.fixture()
def text():
    """Return a sample text string."""
    return 'this is a text'


@pytest.fixture()
def quick_replies():
    """Return a sample list of quick replies."""
    return ['reply 1', 'reply 2', 'reply 3']


@pytest.fixture()
def payload():
    """Return a sample payload dictionary."""
    return {'test key 1': 'test value 1', 'test key 2': 'test value 2'}


@pytest.fixture()
def image_url():
    """Return a sample image URL string."""
    return 'https://test.url/image.jpg'


@pytest.fixture()
def title():
    """Return a sample title string."""
    return 'this is a title'


@pytest.fixture()
def subtitle():
    """Return a sample subtitle string."""
    return 'this is a subtitle'


@pytest.fixture()
def buttons():
    """Return a sample list of card button dictionaries."""
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
    """Return a sample WebhookRequest dictionary."""
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
