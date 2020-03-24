"""Module for QuickReplies rich response"""
from .rich_response import RichResponse


class QuickReplies(RichResponse):  # pylint: disable=too-few-public-methods
    """Dialogflow's Quick Replies class"""

    def __init__(self, quick_replies):
        super().__init__()

        if not (isinstance(quick_replies, list) or isinstance(quick_replies, tuple)):
            raise TypeError('quick_replies argument must be a list or tuple')

        self.quick_replies = quick_replies

    def _get_response_object(self):
        return {'quickReplies': {'quickReplies': self.quick_replies}}
