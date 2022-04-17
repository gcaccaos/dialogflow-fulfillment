from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class RichResponse(metaclass=ABCMeta):
    """
    The base (abstract) class for the different types of rich responses.

    See Also:
        For more information about the :class:`RichResponse`, see the
        `Rich response messages`_ section in Dialogflow's documentation.

    .. _Rich response messages: https://cloud.google.com/dialogflow/docs/intents-rich-messages
    """  # noqa: E501

    @abstractmethod
    def _as_dict(self) -> Dict[str, Any]:
        """
        Convert the rich response object to a dictionary.

        See Also:
            For more information about the fields for the different types of
            messages, see the Message_ section in Dialogflow's documentation.

        .. _Message: https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#message
        """  # noqa: E501

    @classmethod
    @abstractmethod
    def _from_dict(cls, message: Dict[str, Any]) -> 'RichResponse':
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

        See Also:
            For more information about the fields for the different types of
            messages, see the Message_ section in Dialogflow's documentation.

        .. _Message: https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#message
        """  # noqa: E501
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
