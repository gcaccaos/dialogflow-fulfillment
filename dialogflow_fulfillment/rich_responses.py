"""Dialogflow's Rich Response classes module"""


class RichResponse: # pylint: disable=too-few-public-methods
    """Dialogflow's Rich Response class"""

    def _get_response_object(self):
        """Gets the v2 response object"""


class Text(RichResponse): # pylint: disable=too-few-public-methods
    """Dialogflow's Text class"""

    def __init__(self, text):
        super().__init__()

        if not isinstance(text, str):
            raise TypeError('text argument must be a string')

        self.text = text

    def _get_response_object(self):
        return {'text': {'text': [self.text]}}


class QuickReplies(RichResponse): # pylint: disable=too-few-public-methods
    """Dialogflow's Quick Replies class"""

    def __init__(self, quick_replies):
        super().__init__()

        if not all(isinstance(reply, str) for reply in quick_replies):
            raise TypeError('quick_replies argument must be a list or tuple of strings')

        self.quick_replies = quick_replies

    def _get_response_object(self):
        return {'quickReplies': {'quickReplies': self.quick_replies}}


class Payload(RichResponse):
    """Dialogflow's Payload class"""
    def __init__(self, payload):
        super().__init__()

        self.set_payload(payload)

    def set_payload(self, payload):
        """Sets the payload content"""
        if not isinstance(payload, dict):
            raise TypeError('payload argument must be a dictionary')

        self.payload = payload

    def _get_response_object(self):
        return {'payload': self.payload}

class Image(RichResponse):
    """Dialogflow's Image class"""
    def __init__(self, image_uri):
        super().__init__()

        self.set_image(image_uri)

    def set_image(self, image_url):
        """Sets the image URI"""
        if not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self.image_url = image_url

    def _get_response_object(self):
        return {'image': {'imageUri': self.image_url}}
