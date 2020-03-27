"""Module for Image rich response"""
from .rich_response import RichResponse


class Image(RichResponse):
    """
    Dialogflows' image response

    Parameters:
        image_url (str): The image's URL

    Attributes:
        image_url (str): The image's URL
    """

    def __init__(self, image_url: str):
        super().__init__()

        self.set_image(image_url)

    def set_image(self, image_url: str):
        """
        Sets the image URL

        Parameters:
            image_url (str): The image's URL

        Raises:
            TypeError: `image_url` argument must be a string
        """
        if not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self.image_url = image_url

    def _get_response_object(self):
        return {'image': {'imageUri': self.image_url}}
