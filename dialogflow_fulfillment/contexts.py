"""Dialogflow's Context API class module"""


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

        self._index = None
        self._context_array = None
        self.session = session
        self.input_contexts = self._process_input_contexts(input_contexts)
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

        """
        Gets a context from the Dialogflow webhook request

        Parameters:
            name (str): Name of the context

        Returns:
            Optional[Dict]: Context's dictionary
        """
        return self.contexts.get(name)

        """
        Deletes a context a Dialogflow session (set the lifespan to 0)

        Parameters:
            name (str): Name of the context
        """

    def get_output_contexts_array(self):
        """Get array of context objects"""
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
