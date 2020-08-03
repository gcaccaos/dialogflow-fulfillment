from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple, Union


class RichResponse(ABC):
    """The base (abstract) class for the different types of rich responses."""

    @abstractmethod
    def _get_response_object(self) -> Dict:
        """Returns the response object as a dictionary."""


class Card(RichResponse):
    """
    Sends a card response to the end-user.

    Parameters:
        title (str, optional): The title of the card response.
        subtitle (str, optional): The subtitle of the card response. Defaults
        image_url (str, optional): The URL of the card response's image.
        buttons (list(dict(str, str)), optional): The buttons of the card
            response.

    Attributes:
        title (str, optional): The title of the card response.
        subtitle (str, optional): The subtitle of the card response.
        image_url (str, optional): The URL of the card response's image.
        buttons (list(dict(str, str)), optional): The buttons of the card
            response.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        image_url: Optional[str] = None,
        buttons: Optional[List[Dict[str, str]]] = None
    ) -> None:
        super().__init__()

        self.set_title(title)
        self.set_subtitle(subtitle)
        self.set_image(image_url)
        self.set_buttons(buttons)

    def set_title(self, title: Optional[str] = None) -> None:
        """
        Sets the title of the card response.

        Parameters:
            title (str, optional): The title of the card response.

        Raises:
            TypeError: :attr:`title` argument must be a string.
        """
        if title is not None and not isinstance(title, str):
            raise TypeError('title argument must be a string')

        self.title = title

    def set_subtitle(self, subtitle: Optional[str] = None) -> None:
        """
        Sets the subtitle of the card response.

        Parameters:
            subtitle (str, optional): The subtitle of the card response.

        Raises:
            TypeError: :attr:`subtitle` argument must be a string.
        """
        if subtitle is not None and not isinstance(subtitle, str):
            raise TypeError('subtitle argument must be a string')

        self.subtitle = subtitle

    def set_image(self, image_url: Optional[str] = None) -> None:
        """
        Sets the URL of the card response's image.

        Parameters:
            image_url (str, optional): The URL of the card response's image.

        Raises:
            TypeError: :attr:`image_url` argument must be a string.
        """
        if image_url is not None and not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self.image_url = image_url

    def set_buttons(
        self,
        buttons: Optional[List[Dict[str, str]]] = None
    ) -> None:
        """
        Sets the buttons of the card response.

        Parameters:
            buttons (list(dict(str, str)), optional): The buttons of the card
                response.

        Raises:
            TypeError: :attr:`buttons` argument must be a list of buttons.
        """
        if buttons is not None and not isinstance(buttons, list):
            raise TypeError('buttons argument must be a list of buttons')

        self.buttons = self._validate_buttons(buttons)

    @staticmethod
    def _validate_buttons(buttons: Optional[List]) -> List[Dict[str, str]]:
        if buttons is None:
            return None

        validated_buttons = []

        for button in buttons:
            if not isinstance(button, dict):
                raise TypeError('button must be a dictionary')

            text = button.get('text')
            postback = button.get('postback')

            if text is not None and not isinstance(text, str):
                raise TypeError('text argument must be a string')

            if postback is not None and not isinstance(text, str):
                raise TypeError('postback argument must be a string')

            validated_button = {}

            if text is not None:
                validated_button.update({'text': text})

            if postback is not None:
                validated_button.update({'postback': postback})

            validated_buttons.append(validated_button)

        return validated_buttons

    def _get_response_object(self) -> Dict:
        fields = {}

        if self.title is not None:
            fields.update({'title': self.title})

        if self.subtitle is not None:
            fields.update({'subtitle': self.subtitle})

        if self.image_url is not None:
            fields.update({'imageUri': self.image_url})

        if self.buttons is not None:
            fields.update({'buttons': self.buttons})

        return {'card': fields}


class Image(RichResponse):
    """
    Sends an image response to the end-user.

    Parameters:
        image_url (str, optional): The URL of the image response.

    Attributes:
        image_url (str, optional): The URL of the image response.
    """

    def __init__(self, image_url: Optional[str] = None) -> None:
        super().__init__()

        self.set_image(image_url)

    def set_image(self, image_url: Optional[str] = None) -> None:
        """
        Sets the URL of the image response.

        Parameters:
            image_url (str, optional): The URL of the image response.

        Raises:
            TypeError: :attr:`image_url` argument must be a string.
        """
        if image_url is not None and not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self.image_url = image_url

    def _get_response_object(self) -> Dict:
        fields = {}

        if self.image_url is not None:
            fields.update({'imageUri': self.image_url})

        return {'image': fields}


class Payload(RichResponse):
    """
    Sends a custom payload response to the end-user.

    This type of response allows to handle advanced (custom) responses.

    Parameters:
        payload (dict, optional): The content of the custom payload response.

    Attributes:
        payload (dict, optional): The content of the custom payload response.
    """

    def __init__(self, payload: Optional[Dict] = None) -> None:
        super().__init__()

        self.set_payload(payload)

    def set_payload(self, payload: Optional[Dict] = None) -> None:
        """
        Sets the content of the custom payload response.

        Parameters:
            payload (dict, optional): The content of the custom payload
                response.

        Raises:
            TypeError: :attr:`payload` argument must be a dictionary.
        """
        if payload is not None and not isinstance(payload, dict):
            raise TypeError('payload argument must be a dictionary')

        self.payload = payload

    def _get_response_object(self) -> Dict:
        fields = {}

        if self.payload is not None:
            fields.update(self.payload)

        return {'payload': fields}


class QuickReplies(RichResponse):
    """
    Sends quick reply buttons to the end-user.

    When clicked, the button sends the reply text to Dialogflow.

    Parameters:
        title (str, optional): The title of the quick reply buttons.
        quick_replies (list(str) or tuple(str), optional): The texts for
            the quick reply buttons.

    Attributes:
        title (str, optional): The title of the quick reply buttons.
        quick_replies (list(str) or tuple(str), optional): The texts for
            the quick reply buttons.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        quick_replies: Optional[Union[List[str], Tuple[str]]] = None
    ) -> None:
        super().__init__()

        self.set_title(title)
        self.set_quick_replies(quick_replies)

    def set_title(self, title: Optional[str] = None):
        """
        Sets the title of the quick reply buttons.

        Parameters:
            title (str, optional): The title of the quick reply buttons.

        Raises:
            TypeError: :attr:`title` argument must be a string.
        """
        if title is not None and not isinstance(title, str):
            raise TypeError('title argument must be a string')

        self.title = title

    def set_quick_replies(
        self,
        quick_replies: Optional[Union[List[str], Tuple[str]]] = None
    ) -> None:
        """
        Sets the texts for the quick reply buttons.

        Parameters:
            quick_replies (list(str) or tuple(str), optional): The texts for
                the quick reply buttons.

        Raises:
            TypeError: :attr:`quick_replies` argument must be a list or tuple.
        """

        if quick_replies is not None and not isinstance(quick_replies,
                                                        (list, tuple)):
            raise TypeError('quick_replies argument must be a list or tuple')

        self.quick_replies = quick_replies

    def _get_response_object(self) -> Dict:
        fields = {}

        if self.title is not None:
            fields.update({'title': self.title})

        if self.quick_replies is not None:
            fields.update({'quickReplies': self.quick_replies})

        return {'quickReplies': fields}


class Text(RichResponse):
    """
    Sends a basic (static) text response to the end-user.

    Parameters:
        text (:obj:`str`, optional): The content of the text response.

    Attributes:
        text (Optional[str]): The content of the text response.
    """

    def __init__(self, text: Optional[str] = None) -> None:
        super().__init__()

        self.set_text(text)

    def set_text(self, text: Optional[str] = None) -> None:
        """
        Sets the content of the text response.

        Parameters:
            text (:obj:`str`, optional): The content of the text response.

        Raises:
            TypeError: :attr:`text` argument must be a string.
        """
        if text is not None and not isinstance(text, str):
            raise TypeError('text argument must be a string')

        self.text = text

    def _get_response_object(self) -> Dict:
        return {'text': {'text': [self.text if self.text is not None else '']}}
