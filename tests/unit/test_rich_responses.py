import pytest

from dialogflow_fulfillment import (Card, Image, Payload, QuickReplies,
                                    RichResponse, Text)


class TestText:
    def test_non_string(self, text):
        with pytest.raises(TypeError):
            Text({'this': ['is not a text']})

    def test_set_text_with_deprecation_warning(self, text):
        text_obj = Text()

        with pytest.warns(DeprecationWarning):
            text_obj.set_text(text)

        assert text_obj.text == text

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

    def test_set_title_with_deprecation_warning(self, title):
        quick_replies_obj = QuickReplies()

        with pytest.warns(DeprecationWarning):
            quick_replies_obj.set_title(title)

        assert quick_replies_obj.title == title

    def test_non_sequence_replies(self):
        with pytest.raises(TypeError):
            QuickReplies(quick_replies='this is not a sequence')

    def test_set_quick_replies_with_deprecation_warning(self, quick_replies):
        quick_replies_obj = QuickReplies()

        with pytest.warns(DeprecationWarning):
            quick_replies_obj.set_quick_replies(quick_replies)

        assert quick_replies_obj.quick_replies == quick_replies

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

    def test_set_payload_with_deprecation_warning(self, payload):
        payload_obj = Payload()

        with pytest.warns(DeprecationWarning):
            payload_obj.set_payload(payload)

        assert payload_obj.payload == payload

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

    def test_set_image_with_deprecation_warning(self, image_url):
        image_obj = Image()

        with pytest.warns(DeprecationWarning):
            image_obj.set_image(image_url)

        assert image_obj.image_url == image_url

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

    def test_set_title_with_deprecation_warning(self, title):
        card_obj = Card()

        with pytest.warns(DeprecationWarning):
            card_obj.set_title(title)

        assert card_obj.title == title

    def test_subtitle_non_string(self):
        with pytest.raises(TypeError):
            Card(subtitle={'this': ['is not a string']})

    def test_set_subtitle_with_deprecation_warning(self, subtitle):
        card_obj = Card()

        with pytest.warns(DeprecationWarning):
            card_obj.set_subtitle(subtitle)

        assert card_obj.subtitle == subtitle

    def test_image_url_non_string(self):
        with pytest.raises(TypeError):
            Card(image_url={'this': ['is not a string']})

    def test_set_image_with_deprecation_warning(self, image_url):
        card_obj = Card()

        with pytest.warns(DeprecationWarning):
            card_obj.set_image(image_url)

        assert card_obj.image_url == image_url

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

    def test_set_buttons_with_deprecation_warning(self, buttons):
        card_obj = Card()

        with pytest.warns(DeprecationWarning):
            card_obj.set_buttons(buttons)

        assert card_obj.buttons == buttons

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
