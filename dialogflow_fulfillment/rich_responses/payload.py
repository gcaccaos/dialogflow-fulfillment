"""Module for Payload rich response"""
from typing import Dict

from .rich_response import RichResponse


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
