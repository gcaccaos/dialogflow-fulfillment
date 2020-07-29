import pytest

from dialogflow_fulfillment import (Card, Image, Payload, QuickReplies,
                                    RichResponse, Text)


# Tests for Text response
@pytest.fixture
def text():
    return 'this is a text'


def test_text_non_string(text):
    with pytest.raises(TypeError):
        Text({'this': ['is not a text']})


def test_text_as_dict(text):
    text_obj = Text(text)

    assert text_obj._get_response_object() == {'text': {'text': [text]}}


# Tests for QuickReplies response
@pytest.fixture
def quick_replies_title():
    return 'this is a title'

@pytest.fixture
def quick_replies():
    return ['reply 1', 'reply 2', 'reply 3']


def test_quick_replies_empty_params():
    quick_replies_obj = QuickReplies()

    assert quick_replies_obj._get_response_object() == {'quickReplies': {}}


def test_quick_replies_non_string():
    with pytest.raises(TypeError):
        QuickReplies(title={'this': ['is not a string']})


def test_quick_replies_non_sequence_replies():
    with pytest.raises(TypeError):
        QuickReplies(quick_replies='this is not a sequence')


def test_quick_replies_as_dict(quick_replies_title, quick_replies):
    quick_replies_obj = QuickReplies(quick_replies_title, quick_replies)

    assert quick_replies_obj._get_response_object() == {'quickReplies': {'title': quick_replies_title, 'quickReplies': quick_replies}}


# Tests for Payload response
@pytest.fixture
def payload():
    return {'test key 1': 'test value 1', 'test key 2': 'test value 2'}


def test_payload_empty_params():
    payload_obj = Payload()

    assert payload_obj._get_response_object() == {'payload': {}}


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


def test_image_empty_params():
    image_obj = Image()

    assert image_obj._get_response_object() == {'image': {}}


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

@pytest.fixture
def subtitle():
    return 'this is a subtitle'

@pytest.fixture
def buttons():
    return [{'text': 'text 1', 'postback': 'postback 1'}, {'text': 'text 2', 'postback': 'postback 2'}]

def test_card_empty_params():
    card_obj = Card()

    assert card_obj._get_response_object() == {'card': {}}


def test_title_non_string():
    with pytest.raises(TypeError):
        Card(title={'this': ['is not a string']})


def test_subtitle_non_string():
    with pytest.raises(TypeError):
        Card(subtitle={'this': ['is not a string']})


def test_card_image_url_non_string():
    with pytest.raises(TypeError):
        Card(image_url={'this': ['is not a string']})


def test_card_buttons_non_list():
    with pytest.raises(TypeError):
        Card(buttons='this is not a list of buttons')


def test_card_buttons_non_dict():
    with pytest.raises(TypeError):
        Card(buttons=['this is not a button'])


def test_card_button_text_non_string():
    with pytest.raises(TypeError):
        Card(buttons=[{'text': ['this is not a text']}])


def test_card_button_postback_non_string():
    with pytest.raises(TypeError):
        Card(buttons=[{'postback': ['this is not a text']}])


def test_card_button_empty_params():
    card_obj = Card(buttons=[{}])

    assert card_obj._get_response_object() == {'card': {'buttons': [{}]}}


def test_card_as_dict(title, subtitle, image_url, buttons):
    card_obj = Card(title=title, subtitle=subtitle, image_url=image_url, buttons=buttons)

    assert card_obj._get_response_object() == {'card': {'title': title, 'subtitle': subtitle, 'imageUri': image_url, 'buttons': buttons}}


# Tests for the base RichResponse class
def test_base_rich_response_instantiation():
    with pytest.raises(TypeError):
        RichResponse()
