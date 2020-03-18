"""Dialogflow's Context API class module"""


class Context:
    """Dialogflow's Context API class"""

    def __init__(self, input_contexts, session):
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

    def set_(self, name, lifespan_count=None, parameters=None):
        """Set a new Dialogflow outgoing context"""
        if not isinstance(name, str):
            raise TypeError('name argument must be a string')

        if name not in self.contexts:
            self.contexts[name] = {'name': name}

        if lifespan_count is not None:
            self.contexts[name]['lifespanCount'] = lifespan_count

        if parameters is not None:
            self.contexts[name]['parameters'] = parameters

    def get(self, name):
        """Get an context from the Dialogflow webhook request"""
        return self.contexts.get(name)

    def delete(self, name):
        """Delete an context a Dialogflow session (set the lifespan to 0)"""
        self.set_(name, lifespan_count=0)

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
