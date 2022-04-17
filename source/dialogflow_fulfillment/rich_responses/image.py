from typing import Any, Dict, Optional
from warnings import warn

from .base import RichResponse


class Image(RichResponse):
    """
    Send an image response to the end-user.

    Examples:
        Constructing an image response:

            >>> image = Image('https://picsum.photos/200/300.jpg')

    Parameters:
        image_url (str, optional): The URL of the image response.

    See Also:
        For more information about the :class:`Image` response, see the
        `Image responses`_ section in Dialogflow's documentation.

    .. _Image responses: https://cloud.google.com/dialogflow/docs/intents-rich-messages#image
    """  # noqa: E501

    def __init__(self, image_url: Optional[str] = None) -> None:
        super().__init__()

        self.image_url = image_url

    @property
    def image_url(self) -> Optional[str]:
        """
        str, optional: The URL of the image response.

        Examples:
            Accessing the :attr:`image_url` attribute:

                >>> image.image_url
                'https://picsum.photos/200/300.jpg'

            Assigning a value to the :attr:`image_url` attribute:

                >>> image.image_url = 'https://picsum.photos/200/300?blur.jpg'
                >>> image.image_url
                'https://picsum.photos/200/300?blur.jpg'

        Raises:
            TypeError: If the value to be assigned is not a string.
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url: Optional[str]) -> None:
        if image_url is not None and not isinstance(image_url, str):
            raise TypeError('image_url argument must be a string')

        self._image_url = image_url

    def set_image(self, image_url: Optional[str] = None) -> None:
        """
        Set the URL of the image response.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`image_url` attribute instead

        Parameters:
            image_url (str, optional): The URL of the image response.

        Warns:
            DeprecationWarning: Assign value to the :attr:`image_url` attribute
                instead.
        """
        warn(
            'set_image() is deprecated; '
            'assign value to the image_url attribute instead',
            DeprecationWarning
        )

        self.image_url = image_url

    @classmethod
    def _from_dict(cls, message: Dict[str, Any]) -> 'Image':
        image_url = message['image'].get('imageUri')

        return cls(image_url=image_url)

    def _as_dict(self) -> Dict[str, Any]:
        fields = {}

        if self.image_url is not None:
            fields['imageUri'] = self.image_url

        return {'image': fields}
