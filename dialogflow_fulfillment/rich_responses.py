"""Dialogflow's Rich Response classes module"""


class RichResponse: # pylint: disable=too-few-public-methods
    """Dialogflow's Rich Response class"""

    def _get_response_object(self):
        """Gets the v2 response object"""


class Text(RichResponse): # pylint: disable=too-few-public-methods
    """Dialogflow's Text class"""

    def __init__(self, text):
        super().__init__()

        if isinstance(text, str):
            self.text = text
        else:
            raise TypeError('text argument must be a string')

    def _get_response_object(self):
        return {'text': {'text': [self.text]}}


class QuickReplies(RichResponse): # pylint: disable=too-few-public-methods
    """Dialogflow's Quick Responses class"""

    def __init__(self, quick_replies):
        super().__init__()

        if all(isinstance(item, str) for item in quick_replies):
            self.quick_replies = quick_replies
        else:
            raise TypeError('quick_replies argument must be a list or tuple of strings')

    def _get_response_object(self):
        return {'quickReplies': {'quickReplies': self.quick_replies}}

class Payload(RichResponse):
    """Dialogflow's Payload class"""
    def __init__(self, payload):
        super().__init__()

        self.set_payload(payload)

    def set_payload(self, payload):
        """Sets the payload contents"""
        if isinstance(payload, dict):
            self.payload = payload
        else:
            raise TypeError('payload argument must be a dictionary')

    def _get_response_object(self):
        return {'payload': self.payload}
