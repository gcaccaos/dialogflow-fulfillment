from typing import Any, Dict, List, Optional
from warnings import warn

from .base import RichResponse


class Card(RichResponse):
    """
    Send a card response to the end-user.

    Examples:
        Constructing a :class:`Card` response:

        >>> card = Card(
        ...     title='What is your favorite color?',
        ...     subtitle='Choose a color',
        ...     buttons=[{'text': 'Red'}, {'text': 'Green'}, {'text': 'Blue'}]
        ... )

    Parameters:
        title (str, optional): The title of the card response.
        subtitle (str, optional): The subtitle of the card response. Defaults
        image_url (str, optional): The URL of the card response's image.
        buttons (list(dict(str, str)), optional): The buttons of the card
            response.

    See Also:
        For more information about the :class:`Card` response, see the
        `Card responses`_ section in Dialogflow's documentation.

    .. _Card responses: https://cloud.google.com/dialogflow/docs/intents-rich-messages#card
    """  # noqa: E501

    def __init__(
        self,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        image_url: Optional[str] = None,
        buttons: Optional[List[Dict[str, str]]] = None
    ) -> None:
        super().__init__()

        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.buttons = buttons

    @property
    def title(self) -> Optional[str]:
        """
        str, optional: The title of the card response.

        Examples:
            Accessing the :attr:`title` attribute:

                >>> card.title
                'What is your favorite color?'

            Assigning value to the :attr:`title` attribute:

                >>> card.title = 'Which color do you like?'
                >>> card.title
                'Which color do you like?'

        Raises:
            TypeError: If the value to be assigned is not a string.
        """
        return self._title

    @title.setter
    def title(self, title: Optional[str]) -> None:
        if title is not None and not isinstance(title, str):
            raise TypeError('title argument must be a string')

        self._title = title

    def set_title(self, title: Optional[str] = None) -> None:
        """
        Set the title of the card response.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`title` attribute instead

        Parameters:
            title (str, optional): The title of the card response.

        Warns:
            DeprecationWarning: Assign value to the :attr:`title` attribute
                instead.
        """
        warn(
            'set_title() is deprecated; '
            'assign value to the title attribute instead',
            DeprecationWarning
        )

        self.title = title

    @property
    def subtitle(self) -> Optional[str]:
        """
        str, optional: The subtitle of the card response.

        Examples:
            Accessing the :attr:`subtitle` attribute:

                >>> card.subtitle
                'Choose a color'

            Assigning value to the :attr:`subtitle` attribute:

                >>> card.subtitle = 'Select a color below'
                >>> card.subtitle
                'Select a color below'

        Raises:
            TypeError: If the value to be assigned is not a string.
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle: Optional[str]) -> None:
        if subtitle is not None and not isinstance(subtitle, str):
            raise TypeError('subtitle argument must be a string')

        self._subtitle = subtitle

    def set_subtitle(self, subtitle: Optional[str] = None) -> None:
        """
        Set the subtitle of the card response.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`subtitle` attribute instead

        Parameters:
            subtitle (str, optional): The subtitle of the card response.

        Warns:
            DeprecationWarning: Assign value to the :attr:`subtitle` attribute
                instead.
        """
        warn(
            'set_subtitle() is deprecated; '
            'assign value to the subtitle attribute instead',
            DeprecationWarning
        )

        self.subtitle = subtitle

    @property
    def image_url(self) -> Optional[str]:
        """
        str, optional: The URL of the card response's image.

        Examples:
            Accessing the :attr:`image_url` attribute:

                >>> card.image_url
                None

            Assigning value to the :attr:`image_url` attribute:

                >>> card.image_url = 'https://picsum.photos/200/300.jpg'
                >>> card.image_url
                'https://picsum.photos/200/300.jpg'

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
        Set the URL of the card response's image.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`image_url` attribute instead

        Parameters:
            image_url (str, optional): The URL of the card response's image.

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

    @property
    def buttons(self) -> Optional[List[Dict[str, str]]]:
        """
        list(dict(str, str)), optional: The buttons of the card response.

        Examples:
            Accessing the :attr:`buttons` attribute:

                >>> card.buttons
                [{'text': 'Red'}, {'text': 'Green'}, {'text': 'Blue'}]

            Assigning value to the :attr:`buttons` attribute:

                >>> card.buttons = [{'text': 'Cyan'}, {'text': 'Magenta'}]
                >>> card.buttons
                [{'text': 'Cyan'}, {'text': 'Magenta'}]

        Raises:
            TypeError: If the value to be assigned is not a list of buttons.
        """  # noqa: D403
        return self._buttons

    @buttons.setter
    def buttons(self, buttons: Optional[List[Dict[str, str]]]) -> None:
        if buttons is not None and not isinstance(buttons, list):
            raise TypeError('buttons argument must be a list of buttons')

        self._buttons = self._validate_buttons(buttons)

    def set_buttons(
        self,
        buttons: Optional[List[Dict[str, str]]] = None
    ) -> None:
        """
        Set the buttons of the card response.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`buttons` attribute instead

        Parameters:
            buttons (list(dict(str, str), optional): The buttons of the card
                response.

        Warns:
            DeprecationWarning: Assign value to the :attr:`buttons` attribute
                instead.
        """
        warn(
            'set_buttons() is deprecated; '
            'assign value to the buttons attribute instead',
            DeprecationWarning
        )

        self.buttons = buttons

    @classmethod
    def _validate_buttons(
        cls,
        buttons: Optional[List[Dict[str, str]]]
    ) -> Optional[List[Dict[str, str]]]:
        if buttons is None:
            return None

        return [cls._validate_button(button) for button in buttons]

    @classmethod
    def _validate_button(cls, button: Dict[str, str]) -> Dict[str, str]:
        if not isinstance(button, dict):
            raise TypeError('button must be a dictionary')

        text = button.get('text')
        postback = button.get('postback')

        if text is not None and not isinstance(text, str):
            raise TypeError('text argument must be a string')

        if postback is not None and not isinstance(text, str):
            raise TypeError('postback argument must be a string')

        validated_button = {}

        if text is not None:
            validated_button.update({'text': text})

        if postback is not None:
            validated_button.update({'postback': postback})

        return validated_button

    @classmethod
    def _from_dict(cls, message: Dict[str, Any]) -> 'Card':
        title = message['card'].get('title')
        subtitle = message['card'].get('subtitle')
        image_url = message['card'].get('imageUri')
        buttons = message['card'].get('buttons')

        return cls(
            title=title,
            subtitle=subtitle,
            image_url=image_url,
            buttons=buttons
        )

    def _as_dict(self) -> Dict[str, Any]:
        fields = {}

        if self.title is not None:
            fields['title'] = self.title

        if self.subtitle is not None:
            fields['subtitle'] = self.subtitle

        if self.image_url is not None:
            fields['imageUri'] = self.image_url

        if self.buttons is not None:
            fields['buttons'] = self.buttons

        return {'card': fields}
