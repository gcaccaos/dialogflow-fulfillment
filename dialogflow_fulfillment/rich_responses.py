from typing import Dict, List, Tuple, Union


class RichResponse:  # pylint: disable=too-few-public-methods
    """Dialogflow's rich response"""

    def _get_response_object(self):
        """Gets the v2 response object"""


class Card(RichResponse):
    """
    Dialogflow's card response

    Parameters:
        title (str): The card's title

    Attributes:
        title (str): The card's title
    """

    def __init__(self, title: str):
        super().__init__()

        self.set_title(title)

    def set_title(self, title: str):
        """
        Sets the card title

        Args:
            title (str): The title of the card

        Raises:
            TypeError: `title` argument must be a string
        """
        if not isinstance(title, str):
            raise TypeError('title argument must be a string')

        self.title = title

    def _get_response_object(self):
        return {'card': {'title': self.title}}


class Image(RichResponse):
    """
    Dialogflows' image response

    Parameters:
        image_url (str): The image's URL

    Attributes:
        image_url (str): The image's URL
    """

    def __init__(self, image_url: str):
        super().__init__()

        self.set_image(image_url)

    def set_image(self, image_url: str):
        """
        Sets the image URL

        Parameters:
            image_url (str): The image's URL

        Raises:
            TypeError: `image_url` argument must be a string
        """
        if not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self.image_url = image_url

    def _get_response_object(self):
        return {'image': {'imageUri': self.image_url}}


class Payload(RichResponse):
    """
    Dialogflow's payload response

    Parameters:
        payload (Dict): The custom payload content

    Attributes:
        payload (Dict): The custom payload content
    """

    def __init__(self, payload: Dict):
        super().__init__()

        self.set_payload(payload)

    def set_payload(self, payload):
        """
        Sets the payload content

        Parameters:
            payload (Dict): The custom payload content

        Raises:
            TypeError: `payload` argument must be a dictionary
        """
        if not isinstance(payload, dict):
            raise TypeError('payload argument must be a dictionary')

        self.payload = payload

    def _get_response_object(self):
        return {'payload': self.payload}


class QuickReplies(RichResponse):  # pylint: disable=too-few-public-methods
    """
    Dialogflow's quick replies response

    Parameters:
        quick_replies (Union[List[str], Tuple[str]]): Quick reply strings

    Attributes:
        quick_replies (Union[List[str], Tuple[str]]): Quick reply strings

    Raises:
        TypeError: `quick_replies` argument must be a list or tuple
    """

    def __init__(self, quick_replies: Union[List[str], Tuple[str]]):
        super().__init__()

        if not isinstance(quick_replies, (list, tuple)):
            raise TypeError('quick_replies argument must be a list or tuple')

        self.quick_replies = quick_replies

    def _get_response_object(self):
        return {'quickReplies': {'quickReplies': self.quick_replies}}


class Text(RichResponse):  # pylint: disable=too-few-public-methods
    """
    Dialogflow's text response

    Parameters:
        text (str): The text content

    Attributes:
        text (str): The text content
    """

    def __init__(self, text: str):
        super().__init__()

        if not isinstance(text, str):
            raise TypeError('text argument must be a string')

        self.text = text

    def _get_response_object(self):
        return {'text': {'text': [self.text]}}
