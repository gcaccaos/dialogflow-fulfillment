"""Module for Payload rich response"""
from .rich_response import RichResponse


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
