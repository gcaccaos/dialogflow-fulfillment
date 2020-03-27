"""Dialogflow's Context API class module"""
from typing import Dict, List, Optional


class Context:
    """
    Dialogflow's Context API class

    Parameters:
        input_contexts (List[Dict]): Active contexts during intent detection
        session (str): Request's session id

    Attributes:
        input_contexts (List[Dict]): Active contexts during intent detection
        session (str): Request's session id
        contexts (Dict[str, Dict]): mapping of context names to context dictionaries
    """

    def __init__(self, input_contexts: List[Dict], session: str):
        self._index = None
        self._context_array = None
        self.input_contexts = self._process_input_contexts(input_contexts)
        self.session = session
        self.contexts = self._process_input_contexts(input_contexts)

    @staticmethod
    def _process_input_contexts(input_contexts):
        """Processes a list of Dialogflow input contexts"""
        contexts = {}

        for context in input_contexts:
            name = context['name'].rsplit('/', 1)[-1]
            context['name'] = name
            contexts[name] = context

        return contexts

    def set(self, name: str, lifespan_count: Optional[int] = None, parameters: Optional[Dict] = None):
        """
        Sets a new Dialogflow outgoing context

        Parameters:
            name (str): Context's name
            lifespan_count (Optional[int]): Context's lifespan duration in minutes
            parameters (Optional[Dict]): Context's parameters

        Raises:
            TypeError: `name` argument must be a string
        """
        if not isinstance(name, str):
            raise TypeError('name argument must be a string')

        if name not in self.contexts:
            self.contexts[name] = {'name': name}

        if lifespan_count is not None:
            self.contexts[name]['lifespanCount'] = lifespan_count

        if parameters is not None:
            self.contexts[name]['parameters'] = parameters

    def get(self, name: str) -> Optional[Dict]:
        """
        Gets a context from the Dialogflow webhook request

        Parameters:
            name (str): Name of the context

        Returns:
            Optional[Dict]: Context's dictionary
        """
        return self.contexts.get(name)

    def delete(self, name: str):
        """
        Deletes a context a Dialogflow session (set the lifespan to 0)

        Parameters:
            name (str): Name of the context
        """
        self.set(name, lifespan_count=0)

    def get_output_contexts_array(self) -> List[Dict]:
        """
        Gets the list of context objects

        Returns:
            List[Dict]: Output contexts
        """
        output_contexts = [*self]

        for context in output_contexts:
            context['name'] = f"{self.session}/contexts/{context['name']}"

        return output_contexts

    def __iter__(self):
        self._index = 0
        self._context_array = list(self.contexts.values())

        return self

    def __next__(self):
        if self._index >= len(self._context_array):
            raise StopIteration

        context = self._context_array[self._index]

        self._index += 1

        return context
