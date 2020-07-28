from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union


class RichResponse(ABC):
    """The base (abstract) class for the different types of rich responses."""

    @abstractmethod
    def _get_response_object(self):
        """Returns the response object as a dictionary."""


class Card(RichResponse):
    """
    Sends a card response to the end-user.

    Parameters:
        title (str): The title of the card response.

    Attributes:
        title (str): The title of the card response.
    """

    def __init__(self, title: str) -> None:
        super().__init__()

        self.set_title(title)

    def set_title(self, title: str) -> None:
        """
        Sets the title of the card response.

        Parameters:
            title (str): The title of the card response.

        Raises:
            TypeError: `title` argument must be a string
        """
        if not isinstance(title, str):
            raise TypeError('title argument must be a string')

        self.title = title

    def _get_response_object(self) -> Dict:
        return {'card': {'title': self.title}}


class Image(RichResponse):
    """
    Sends an image response to the end-user.

    Parameters:
        image_url (str): The URL of the image response.

    Attributes:
        image_url (str): The URL of the image response.
    """

    def __init__(self, image_url: str) -> None:
        super().__init__()

        self.set_image(image_url)

    def set_image(self, image_url: str) -> None:
        """
        Sets the URL of the image response.

        Parameters:
            image_url (str): The URL of the image response.

        Raises:
            TypeError: `image_url` argument must be a string
        """
        if not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self.image_url = image_url

    def _get_response_object(self) -> Dict:
        return {'image': {'imageUri': self.image_url}}


class Payload(RichResponse):
    """
    Sends a custom payload response to the end-user.

    This type of response allows to handle advanced (custom) responses.

    Parameters:
        payload (Dict): The content of the custom payload response.

    Attributes:
        payload (Dict): The content of the custom payload response.
    """

    def __init__(self, payload: Dict) -> None:
        super().__init__()

        self.set_payload(payload)

    def set_payload(self, payload: Dict) -> None:
        """
        Sets the content of the custom payload response.

        Parameters:
            payload (Dict): The content of the custom payload response.

        Raises:
            TypeError: `payload` argument must be a dictionary
        """
        if not isinstance(payload, dict):
            raise TypeError('payload argument must be a dictionary')

        self.payload = payload

    def _get_response_object(self) -> Dict:
        return {'payload': self.payload}


class QuickReplies(RichResponse):
    """
    Sends quick reply buttons to the end-user.

    When clicked, the button sends the reply text to Dialogflow.

    Parameters:
        quick_replies (Union[List[str], Tuple[str]]): The texts for the quick
            reply buttons.

    Attributes:
        quick_replies (Union[List[str], Tuple[str]]): The texts for the quick
            reply buttons.

    Raises:
        TypeError: `quick_replies` argument must be a list or tuple
    """

    def __init__(self, quick_replies: Union[List[str], Tuple[str]]) -> None:
        super().__init__()

        if not isinstance(quick_replies, (list, tuple)):
            raise TypeError('quick_replies argument must be a list or tuple')

        self.quick_replies = quick_replies

    def _get_response_object(self) -> Dict:
        return {'quickReplies': {'quickReplies': self.quick_replies}}


class Text(RichResponse):
    """
    Sends a basic (static) text response to the end-user.

    Parameters:
        text (str): The content of the text response.

    Attributes:
        text (str): The content of the text response.
    """

    def __init__(self, text: str) -> None:
        super().__init__()

        self.set_text(text)

    def set_text(self, text: str) -> None:
        """
        Sets the content of the text response.

        Parameters:
            text (str): The content of the text response.
        """
        if not isinstance(text, str):
            raise TypeError('text argument must be a string')

        self.text = text

    def _get_response_object(self) -> Dict:
        return {'text': {'text': [self.text]}}
