from typing import Any, Dict, Optional
from warnings import warn

from .base import RichResponse


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

    def __init__(self, payload: Optional[Dict[Any, Any]] = None) -> None:
        super().__init__()

        self.payload = payload

    @property
    def payload(self) -> Optional[Dict[Any, Any]]:
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
        """  # noqa: D401, E501
        return self._payload

    @payload.setter
    def payload(self, payload: Optional[Dict[Any, Any]]) -> None:
        if payload is not None and not isinstance(payload, dict):
            raise TypeError('payload argument must be a dictionary')

        self._payload = payload

    def set_payload(self, payload: Optional[Dict[Any, Any]] = None) -> None:
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
    def _from_dict(cls, message: Dict[str, Any]) -> 'Payload':
        payload = message['payload']

        return cls(payload=payload)

    def _as_dict(self) -> Dict[str, Any]:
        fields = {}

        if self.payload is not None:
            fields.update(self.payload)

        return {'payload': fields}
