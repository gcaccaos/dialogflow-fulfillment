"""Module for Card rich response"""
from .rich_response import RichResponse


class Card(RichResponse):
    """Dialogflow's Card class"""

    def __init__(self, title):
        super().__init__()

        if not isinstance(title, str):
            raise TypeError('title argument must be a string')

        self.set_title(title)

    def set_title(self, title):
        """Sets the card title"""
        self.title = title

    def _get_response_object(self):
        return {'card': {'title': self.title}}
