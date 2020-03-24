"""Module for Image rich response"""
from .rich_response import RichResponse


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
