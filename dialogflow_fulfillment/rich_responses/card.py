"""Module for Card rich response"""
from .rich_response import RichResponse


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
