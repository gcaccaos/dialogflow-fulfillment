from typing import Any, Dict, List, Optional, Tuple, Union
from warnings import warn

from .base import RichResponse


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
        quick_replies (list, tuple(str), optional): The texts for the quick
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
        list, tuple(str), optional: The texts for the quick reply buttons.

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
        """  # noqa: D403
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
            quick_replies (list, tuple(str), optional): The texts for the
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
    def _from_dict(cls, message: Dict[str, Any]) -> 'QuickReplies':
        title = message['quickReplies'].get('title')
        quick_replies = message['quickReplies'].get('quickReplies')

        return cls(title=title, quick_replies=quick_replies)

    def _as_dict(self) -> Dict[str, Any]:
        fields = {}

        if self.title is not None:
            fields['title'] = self.title

        if self.quick_replies is not None:
            fields['quickReplies'] = self.quick_replies

        return {'quickReplies': fields}
