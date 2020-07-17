import pytest

from dialogflow_fulfillment import Card, Image, Payload, QuickReplies, Text


# Tests for Text response
@pytest.fixture
def text():
    return 'this is a text'


def test_text_attr(text):
    text_obj = Text(text)

    assert text_obj.text == text


def test_text_non_string(text):
    with pytest.raises(TypeError):
        Text({'this': ['is not a text']})


def test_text_as_dict(text):
    text_obj = Text(text)

    assert text_obj._get_response_object() == {'text': {'text': [text]}}


# Tests for QuickReplies response
@pytest.fixture
def quick_replies():
    return ['reply 1', 'reply 2', 'reply 3']


def test_quick_replies_attr(quick_replies):
    quick_replies_obj = QuickReplies(quick_replies)

    assert quick_replies_obj.quick_replies == quick_replies


def test_quick_replies_non_sequence():
    with pytest.raises(TypeError):
        QuickReplies('this is not a sequence')


def test_quick_replies_as_dict(quick_replies):
    quick_replies_obj = QuickReplies(quick_replies)

    assert quick_replies_obj._get_response_object() == {'quickReplies': {'quickReplies': quick_replies}}


# Tests for Payload response
@pytest.fixture
def payload():
    return {'test key 1': 'test value 1', 'test key 2': 'test value 2'}


def test_payload_attr(payload):
    payload_obj = Payload(payload)

    assert payload_obj.payload == payload


def test_payload_non_dict():
    with pytest.raises(TypeError):
        Payload('this is not a dict')


def test_payload_as_dict(payload):
    payload_obj = Payload(payload)

    assert payload_obj._get_response_object() == {'payload': payload}


# Tests for Image response
@pytest.fixture
def image_url():
    return 'https://test.url/image.jpg'


def test_image_url_attr(image_url):
    image_obj = Image(image_url)

    assert image_obj.image_url == image_url


def test_image_url_non_string():
    with pytest.raises(TypeError):
        Image({'this': ['is not a string']})


def test_image_as_dict(image_url):
    image_obj = Image(image_url)

    assert image_obj._get_response_object() == {'image': {'imageUri': image_url}}


# Tests for Card response
@pytest.fixture
def title():
    return 'this is a title'


def test_title_attr(title):
    card_obj = Card(title)

    assert card_obj.title == title


def test_title_non_string():
    with pytest.raises(TypeError):
        Card({'this': ['is not a string']})


def test_card_as_dict(title):
    card_obj = Card(title)

    assert card_obj._get_response_object() == {'card': {'title': title}}
