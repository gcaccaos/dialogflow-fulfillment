"""Module for QuickReplies rich response"""
from typing import List, Tuple, Union

from .rich_response import RichResponse


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

        if not (isinstance(quick_replies, list) or \
                isinstance(quick_replies, tuple)):
            raise TypeError('quick_replies argument must be a list or tuple')

        self.quick_replies = quick_replies

    def _get_response_object(self):
        return {'quickReplies': {'quickReplies': self.quick_replies}}
