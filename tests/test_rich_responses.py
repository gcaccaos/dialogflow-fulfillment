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


def test_text_set_text(text):
    text_obj = Text()

    text_obj.set_text(text)

    assert text_obj.text == text


def test_text_as_dict(text):
    text_obj = Text(text)

    assert text_obj._as_dict() == {'text': {'text': [text]}}


# Tests for QuickReplies response
@pytest.fixture
def quick_replies_title():
    return 'this is a title'

@pytest.fixture
def quick_replies():
    return ['reply 1', 'reply 2', 'reply 3']


def test_quick_replies_empty_params():
    quick_replies_obj = QuickReplies()

    assert quick_replies_obj._as_dict() == {'quickReplies': {}}


def test_quick_replies_non_string_title():
    with pytest.raises(TypeError):
        QuickReplies(title={'this': ['is not a string']})


def test_quick_replies_set_title(quick_replies_title):
    quick_replies_obj = QuickReplies()

    quick_replies_obj.set_title(quick_replies_title)

    assert quick_replies_obj.title == quick_replies_title


def test_quick_replies_non_sequence_replies():
    with pytest.raises(TypeError):
        QuickReplies(quick_replies='this is not a sequence')


def test_quick_replies_set_quick_replies(quick_replies):
    quick_replies_obj = QuickReplies()

    quick_replies_obj.set_quick_replies(quick_replies)

    assert quick_replies_obj.quick_replies == quick_replies


def test_quick_replies_as_dict(quick_replies_title, quick_replies):
    quick_replies_obj = QuickReplies(quick_replies_title, quick_replies)

    assert quick_replies_obj._as_dict() == {'quickReplies': {'title': quick_replies_title, 'quickReplies': quick_replies}}


# Tests for Payload response
@pytest.fixture
def payload():
    return {'test key 1': 'test value 1', 'test key 2': 'test value 2'}


def test_payload_empty_params():
    payload_obj = Payload()

    assert payload_obj._as_dict() == {'payload': {}}


def test_payload_non_dict():
    with pytest.raises(TypeError):
        Payload('this is not a dict')


def test_payload_set_payload(payload):
    payload_obj = Payload()

    payload_obj.set_payload(payload)

    assert payload_obj.payload == payload


def test_payload_as_dict(payload):
    payload_obj = Payload(payload)

    assert payload_obj._as_dict() == {'payload': payload}


# Tests for Image response
@pytest.fixture
def image_url():
    return 'https://test.url/image.jpg'


def test_image_empty_params():
    image_obj = Image()

    assert image_obj._as_dict() == {'image': {}}


def test_image_url_non_string():
    with pytest.raises(TypeError):
        Image({'this': ['is not a string']})


def test_image_set_image(image_url):
    image_obj = Image()

    image_obj.set_image(image_url)

    assert image_obj.image_url == image_url


def test_image_as_dict(image_url):
    image_obj = Image(image_url)

    assert image_obj._as_dict() == {'image': {'imageUri': image_url}}


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

    assert card_obj._as_dict() == {'card': {}}


def test_title_non_string():
    with pytest.raises(TypeError):
        Card(title={'this': ['is not a string']})


def test_card_set_title(title):
    card_obj = Card()

    card_obj.set_title(title)

    assert card_obj.title == title


def test_subtitle_non_string():
    with pytest.raises(TypeError):
        Card(subtitle={'this': ['is not a string']})


def test_card_set_subtitle(subtitle):
    card_obj = Card()

    card_obj.set_subtitle(subtitle)

    assert card_obj.subtitle == subtitle


def test_card_image_url_non_string():
    with pytest.raises(TypeError):
        Card(image_url={'this': ['is not a string']})


def test_card_set_image(image_url):
    card_obj = Card()

    card_obj.set_image(image_url)

    assert card_obj.image_url == image_url


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


def test_card_set_buttons(buttons):
    card_obj = Card()

    card_obj.set_buttons(buttons)

    assert card_obj.buttons == buttons


def test_card_button_empty_params():
    card_obj = Card(buttons=[{}])

    assert card_obj._as_dict() == {'card': {'buttons': [{}]}}


def test_card_as_dict(title, subtitle, image_url, buttons):
    card_obj = Card(title=title, subtitle=subtitle, image_url=image_url, buttons=buttons)

    assert card_obj._as_dict() == {'card': {'title': title, 'subtitle': subtitle, 'imageUri': image_url, 'buttons': buttons}}


# Tests for the base RichResponse class
def test_base_rich_response_instantiation():
    with pytest.raises(TypeError):
        RichResponse()
