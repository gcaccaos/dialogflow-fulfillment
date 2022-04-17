from typing import Any, Dict, List, Optional


class Context:
    """
    A client class for accessing and manipulating input and output contexts.

    This class provides an API that allows to create, edit or delete contexts
    during conversations.

    Parameters:
        input_contexts (list(dict)): The contexts that were active in the
            conversation when the intent was triggered by Dialogflow.
        session (str): The session of the conversation.

    Attributes:
        input_contexts (list(dict)): The contexts that were active in the
            conversation when the intent was triggered by Dialogflow.
        session (str): The session of the conversation.
        contexts (dict(str, dict)): A mapping of context names to context
            objects (dictionaries).
    """

    def __init__(
        self,
        input_contexts: List[Dict[str, Any]],
        session: str
    ) -> None:
        self.input_contexts = self._process_input_contexts(input_contexts)
        self.session = session
        self.contexts = {**self.input_contexts}

    @staticmethod
    def _process_input_contexts(
        input_contexts: List[Dict[str, Any]]
    ) -> Dict[str, Dict[str, Any]]:
        """Process a list of input contexts."""
        contexts = {}

        for context in input_contexts:
            name = context.get('name', '').rsplit('/', 1).pop()
            contexts[name] = context

        return contexts

    def set(
        self,
        name: str,
        lifespan_count: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Set a new context or update an existing context.

        Sets the lifepan and parameters of a context (if the context exists) or
        creates a new output context (if the context doesn't exist).

        Parameters:
            name (str): The name of the context.
            lifespan_count (int, optional): The lifespan duration of the
                context (in minutes).
            parameters (dict, optional): The parameters of the context.

        Raises:
            TypeError: If the name is not a string.
        """
        if not isinstance(name, str):
            raise TypeError('name argument must be a string')

        if name not in self.contexts:
            self.contexts[name] = {'name': name}

        if lifespan_count is not None:
            self.contexts[name]['lifespanCount'] = lifespan_count

        if parameters is not None:
            self.contexts[name]['parameters'] = parameters

    def get(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get the context object (if exists).

        Parameters:
            name (str): The name of the context.

        Returns:
            dict, optional: The context object (dictionary) if exists.
        """
        return self.contexts.get(name)

    def delete(self, name: str) -> None:
        """
        Deactivate an output context by setting its lifespan to 0.

        Parameters:
            name (str): The name of the context.
        """
        self.set(name, lifespan_count=0)

    def get_output_contexts_array(self) -> List[Dict[str, Any]]:
        """
        Get the output contexts as an array.

        Returns:
            list(dict): The output contexts (dictionaries).
        """
        return [*self]

    def __iter__(self) -> 'Context':
        """Implement iter(self)."""
        self._index = 0
        self._context_array = list(self.contexts.values())

        return self

    def __next__(self) -> Dict[str, Any]:
        """Implement next(self)."""
        if self._index >= len(self._context_array):
            raise StopIteration

        context = self._context_array[self._index]

        self._index += 1

        return context
