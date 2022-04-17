from typing import Any, Dict, Optional
from warnings import warn

from .base import RichResponse


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
    def _from_dict(cls, message: Dict[str, Any]) -> 'Text':
        texts = message['text'].get('text', [])
        text = texts[0] if texts else None

        return cls(text=text)

    def _as_dict(self) -> Dict[str, Any]:
        text = self.text

        return {'text': {'text': [text if text is not None else '']}}
