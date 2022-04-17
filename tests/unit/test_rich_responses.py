import pytest
from dialogflow_fulfillment import (
    Card,
    Image,
    Payload,
    QuickReplies,
    RichResponse,
    Text,
)


class TestText:
    def test_non_string(self, text):
        with pytest.raises(TypeError):
            Text({'this': ['is not a text']})

    def test_as_dict(self, text):
        text_obj = Text(text)

        assert text_obj._as_dict() == {'text': {'text': [text]}}


class TestQuickReplies:
    def test_empty_params(self):
        quick_replies_obj = QuickReplies()

        assert quick_replies_obj._as_dict() == {'quickReplies': {}}

    def test_non_string_title(self):
        with pytest.raises(TypeError):
            QuickReplies(title={'this': ['is not a string']})

    def test_non_sequence_replies(self):
        with pytest.raises(TypeError):
            QuickReplies(quick_replies='this is not a sequence')

    def test_as_dict(self, title, quick_replies):
        quick_replies_obj = QuickReplies(title, quick_replies)

        assert quick_replies_obj._as_dict() == {
            'quickReplies': {
                'title': title,
                'quickReplies': quick_replies
            }
        }


class TestPayload:
    def test_empty_params(self):
        payload_obj = Payload()

        assert payload_obj._as_dict() == {'payload': {}}

    def test_non_dict(self):
        with pytest.raises(TypeError):
            Payload('this is not a dict')

    def test_as_dict(self, payload):
        payload_obj = Payload(payload)

        assert payload_obj._as_dict() == {'payload': payload}


class TestImage:
    def test_empty_params(self):
        image_obj = Image()

        assert image_obj._as_dict() == {'image': {}}

    def test_non_string(self):
        with pytest.raises(TypeError):
            Image({'this': ['is not a string']})

    def test_as_dict(self, image_url):
        image_obj = Image(image_url)

        assert image_obj._as_dict() == {'image': {'imageUri': image_url}}


class TestCard:
    def test_empty_params(self):
        card_obj = Card()

        assert card_obj._as_dict() == {'card': {}}

    def test_title_non_string(self):
        with pytest.raises(TypeError):
            Card(title={'this': ['is not a string']})

    def test_subtitle_non_string(self):
        with pytest.raises(TypeError):
            Card(subtitle={'this': ['is not a string']})

    def test_image_url_non_string(self):
        with pytest.raises(TypeError):
            Card(image_url={'this': ['is not a string']})

    def test_buttons_non_list(self):
        with pytest.raises(TypeError):
            Card(buttons='this is not a list of buttons')

    def test_buttons_non_dict(self):
        with pytest.raises(TypeError):
            Card(buttons=['this is not a button'])

    def test_button_text_non_string(self):
        with pytest.raises(TypeError):
            Card(buttons=[{'text': ['this is not a text']}])

    def test_button_postback_non_string(self):
        with pytest.raises(TypeError):
            Card(buttons=[{'postback': ['this is not a text']}])

    def test_button_empty_params(self):
        card_obj = Card(buttons=[{}])

        assert card_obj._as_dict() == {'card': {'buttons': [{}]}}

    def test_as_dict(self, title, subtitle, image_url, buttons):
        card_obj = Card(
            title=title,
            subtitle=subtitle,
            image_url=image_url,
            buttons=buttons
        )

        assert card_obj._as_dict() == {
            'card': {
                'title': title,
                'subtitle': subtitle,
                'imageUri': image_url,
                'buttons': buttons
            }
        }


class TestRichResponse:
    def test_instantiation(self):
        with pytest.raises(TypeError):
            RichResponse()
