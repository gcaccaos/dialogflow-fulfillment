from abc import ABCMeta, abstractmethod
from typing import Dict, List, Optional, Tuple, Union
from warnings import warn


class RichResponse(metaclass=ABCMeta):
    """
    The base (abstract) class for the different types of rich responses.

    See Also:
        For more information about the :class:`RichResponse`, see the
        `Rich response messages`_ section in Dialogflow's documentation.

    .. _Rich response messages: https://cloud.google.com/dialogflow/docs/intents-rich-messages
    """  # noqa: E501

    @abstractmethod
    def _as_dict(self) -> Dict:
        """Convert the rich response object to a dictionary."""

    @classmethod
    @abstractmethod
    def _from_dict(cls, message: Dict) -> 'RichResponse':
        """
        Convert a response message object to a type of :class:`RichResponse`.

        Parameters:
            message (dict): The response message object from Dialogflow.

        Returns:
            :class:`RichResponse`: A subclass of :class:`RichResponse` that
            corresponds to the message field in the message object (e.g.: it
            creates an instance of a :class:`QuickReplies` if the response
            message object has a :obj:`quickReplies` field).

        Raises:
            TypeError: If the response message object doesn't have exactly one
                field for a supported type of message.
        """
        message_fields_to_classes = {
            cls._upper_camel_to_lower_camel(subclass.__name__): subclass
            for subclass in cls.__subclasses__()
        }

        fields_intersection = message.keys() & message_fields_to_classes.keys()

        if not len(fields_intersection) == 1:
            raise TypeError('unsupported type of message')

        message_field = fields_intersection.pop()

        return message_fields_to_classes[message_field]._from_dict(message)

    @classmethod
    def _upper_camel_to_lower_camel(cls, name: str) -> str:
        """
        Convert a UpperCamelCase name to lowerCamelCase.

        Parameters:
            name (str): A UpperCamelCase string.

        Returns:
            str: The input string in lowerCamelCase.
        """
        return name[0].lower() + name[1:]


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
        buttons (list of dict(str, str), optional): The buttons of the card
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
        list of dict(str, str), optional: The buttons of the card response.

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
        """
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
            buttons (list of dict(str, str), optional): The buttons of the card
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
    def _from_dict(cls, message: Dict) -> 'Card':
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

    def _as_dict(self) -> Dict:
        fields = {}

        if self.title is not None:
            fields.update({'title': self.title})

        if self.subtitle is not None:
            fields.update({'subtitle': self.subtitle})

        if self.image_url is not None:
            fields.update({'imageUri': self.image_url})

        if self.buttons is not None:
            fields.update({'buttons': self.buttons})

        return {'card': fields}


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
    def _from_dict(cls, message: Dict) -> 'Image':
        image_url = message['image'].get('imageUri')

        return cls(image_url=image_url)

    def _as_dict(self) -> Dict:
        fields = {}

        if self.image_url is not None:
            fields.update({'imageUri': self.image_url})

        return {'image': fields}


class Payload(RichResponse):
    """
    Send a custom payload response to the end-user.

    This type of rich response allows to create advanced, custom, responses.

    Examples:
        Constructing a custom :class:`Payload` response for file attachments:

        >>> payload_data = {
        ...     'attachment': 'https://example.com/files/some_file.pdf',
        ...     'type': 'application/pdf'
        ... }
        >>> payload = Payload(payload_data)

    Parameters:
        payload (dict, optional): The content of the custom payload response.

    See Also:
        For more information about the :class:`Payload` response, see the
        `Custom payload responses`_ section in Dialogflow's documentation.

    .. _Custom payload responses: https://cloud.google.com/dialogflow/docs/intents-rich-messages#custom
    """  # noqa: E501

    def __init__(self, payload: Optional[Dict] = None) -> None:
        super().__init__()

        self.payload = payload

    @property
    def payload(self) -> Optional[Dict]:
        """
        dict, optional: The content of the custom payload response.

        Examples:
            Accessing the :attr:`payload` attribute:

                >>> payload.payload
                {'attachment': 'https://example.com/files/some_file.pdf', 'type': 'application/pdf'}

            Assigning a value to the :attr:`payload` attribute:

                >>> payload.payload = {
                ...     'attachment': 'https://example.com/files/another_file.zip',
                ...     'type': 'application/zip'
                ... }
                >>> payload.payload
                {'attachment': 'https://example.com/files/another_file.zip', 'type': 'application/zip'}

        Raises:
            TypeError: If the value to be assigned is not a dictionary.
        """  # noqa: E501
        return self._payload

    @payload.setter
    def payload(self, payload: Optional[Dict]) -> None:
        if payload is not None and not isinstance(payload, dict):
            raise TypeError('payload argument must be a dictionary')

        self._payload = payload

    def set_payload(self, payload: Optional[Dict] = None) -> None:
        """
        Set the content of the custom payload response.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`payload` attribute instead.

        Parameters:
            payload (dict, optional): The content of the custom payload
                response.

        Warns:
            DeprecationWarning: Assign value to the :attr:`payload` attribute
                instead.
        """
        warn(
            'set_payload() is deprecated; '
            'assign value to the payload attribute instead',
            DeprecationWarning
        )

        self.payload = payload

    @classmethod
    def _from_dict(cls, message: Dict) -> 'Payload':
        payload = message['payload']

        return cls(payload=payload)

    def _as_dict(self) -> Dict:
        fields = {}

        if self.payload is not None:
            fields.update(self.payload)

        return {'payload': fields}


class QuickReplies(RichResponse):
    """
    Send a collection of quick replies to the end-user.

    When a quick reply button is clicked, the corresponding reply text is sent
    back to Dialogflow as if the user had typed it.

    Examples:
        Constructing a :class:`QuickReplies` response:

            >>> quick_replies = QuickReplies('Choose an answer', ['Yes', 'No'])

    Parameters:
        title (str, optional): The title of the quick reply buttons.
        quick_replies (list or tuple of str, optional): The texts for the quick
            reply buttons.

    See Also:
        For more information about the :class:`QuickReplies` response, see the
        `Quick reply responses`_ section in Dialogflow's documentation.

    .. _Quick reply responses: https://cloud.google.com/dialogflow/docs/intents-rich-messages#quick
    """  # noqa: E501

    def __init__(
        self,
        title: Optional[str] = None,
        quick_replies: Optional[Union[List[str], Tuple[str]]] = None
    ) -> None:
        super().__init__()

        self.title = title
        self.quick_replies = quick_replies

    @property
    def title(self) -> Optional[str]:
        """
        str, optional: The title of the quick reply buttons.

        Examples:
            Accessing the :attr:`title` attribute:

                >>> quick_replies.title
                'Choose an answer'

            Assigning a value to the :attr:`title` attribute:

                >>> quick_replies.title = 'Select yes or no'
                >>> quick_replies.title
                'Select yes or no'

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
        Set the title of the quick reply buttons.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`title` attribute instead.

        Parameters:
            title (str, optional): The title of the quick reply buttons.

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
    def quick_replies(self) -> Optional[Union[List[str], Tuple[str]]]:
        """
        list or tuple of str, optional: The texts for the quick reply buttons.

        Examples:
            Accessing the :attr:`quick_replies` attribute:

                >>> quick_replies.quick_replies
                ['Yes', 'No']

            Assigning a value to the :attr:`quick_replies` attribute:

                >>> quick_replies.quick_replies = ['Yes', 'No', 'Maybe']
                >>> quick_replies.quick_replies
                ['Yes', 'No', 'Maybe']

        Raises:
            TypeError: if the value to be assigned is not a list or tuple of
                strings.
        """
        return self._quick_replies

    @quick_replies.setter
    def quick_replies(
        self,
        quick_replies: Optional[Union[List[str], Tuple[str]]]
    ) -> None:
        if quick_replies is not None and not isinstance(quick_replies,
                                                        (list, tuple)):
            raise TypeError('quick_replies argument must be a list or tuple')

        self._quick_replies = quick_replies

    def set_quick_replies(
        self,
        quick_replies: Optional[Union[List[str], Tuple[str]]] = None
    ) -> None:
        """
        Set the texts for the quick reply buttons.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`quick_replies` attribute instead.

        Parameters:
            quick_replies (list or tuple of str, optional): The texts for the
                quick reply buttons.

        Warns:
            DeprecationWarning: Assign value to the :attr:`quick_replies`
                attribute instead.
        """
        warn(
            'set_quick_replies() is deprecated; '
            'assign value to the quick_replies attribute instead',
            DeprecationWarning
        )

        self.quick_replies = quick_replies

    @classmethod
    def _from_dict(cls, message: Dict) -> 'QuickReplies':
        title = message['quickReplies'].get('title')
        quick_replies = message['quickReplies'].get('quickReplies')

        return cls(title=title, quick_replies=quick_replies)

    def _as_dict(self) -> Dict:
        fields = {}

        if self.title is not None:
            fields.update({'title': self.title})

        if self.quick_replies is not None:
            fields.update({'quickReplies': self.quick_replies})

        return {'quickReplies': fields}


class Text(RichResponse):
    """
    Send a basic (static) text response to the end-user.

    Examples:
        Constructing a :class:`Text` response:

            >>> text = Text('this is a text response')

    Parameters:
        text (str, optional): The content of the text response.

    See Also:
        For more information about the :class:`Text` response, see the
        `Text responses`_ section in Dialogflow's documentation.

    .. _Text responses: https://cloud.google.com/dialogflow/docs/intents-rich-messages#text
    """  # noqa: E501

    def __init__(self, text: Optional[str] = None) -> None:
        super().__init__()

        self.text = text

    @property
    def text(self) -> Optional[str]:
        """
        str, optional: The content of the text response.

        Examples:
            Accessing the :attr:`text` attribute:

                >>> text.text
                'this is a text response'

            Assigning a value to the :attr:`text` attribute:

                >>> text.text = 'this is a new text response'
                >>> text.text
                'this is a new text response'

        Raises:
            TypeError: If the value to be assigned is not a string.
        """
        return self._text

    @text.setter
    def text(self, text: Optional[str]) -> None:
        if text is not None and not isinstance(text, str):
            raise TypeError('text argument must be a string')

        self._text = text

    def set_text(self, text: Optional[str] = None) -> None:
        """
        Set the content of the text response.

        Warning:
            This method is deprecated and will be removed. Assign value to the
            :attr:`text` attribute instead.

        Parameters:
            text (str, optional): The content of the text response.

        Warns:
            DeprecationWarning: Assign value to the :attr:`text` attribute
                instead.
        """
        warn(
            'set_text() is deprecated; '
            'assign value to the text attribute instead',
            DeprecationWarning
        )

        self.text = text

    @classmethod
    def _from_dict(cls, message: Dict) -> 'Text':
        texts = message['text'].get('text', [])
        text = texts[0] if texts else None

        return cls(text=text)

    def _as_dict(self) -> Dict:
        text = self.text

        return {'text': {'text': [text if text is not None else '']}}
