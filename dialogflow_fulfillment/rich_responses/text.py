"""Module for Text rich response"""
from .rich_response import RichResponse


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
