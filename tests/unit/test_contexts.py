import pytest

from dialogflow_fulfillment.contexts import Context


def test_get(session):
    contexts = [
        {
            'name': f'projects/PROJECT_ID/agent/sessions/{session}/contexts/__system_counters__',  # noqa: E501
            'parameters': {
                'no-input': 0,
                'no-match': 0
            }
        }
    ]

    context_api = Context(contexts, session)

    assert context_api.get('a undefined context') is None


def test_delete(session):
    contexts = [
        {
            'name': f'projects/PROJECT_ID/agent/sessions/{session}/contexts/__system_counters__',  # noqa: E501
            'parameters': {
                'no-input': 0,
                'no-match': 0
            }
        },
        {
            'name': f'projects/PROJECT_ID/agent/sessions/{session}/contexts/another_context',  # noqa: E501
            'lifespanCount': 1,
            'parameters': {}
        }
    ]

    context_api = Context(contexts, session)

    context_api.delete('another_context')

    assert context_api.get('another_context')['lifespanCount'] == 0


def test_set_non_string(session):
    context_api = Context([], session)

    with pytest.raises(TypeError):
        context_api.set({'this': 'is not a string'})


def test_set_new_context(session):
    context_api = Context([], session)

    context_api.set('new_context')

    assert 'new_context' in context_api.contexts


def test_set_parameters(session):
    contexts = [
        {
            'name': f'projects/PROJECT_ID/agent/sessions/{session}/contexts/__system_counters__',  # noqa: E501
            'parameters': {
                'no-input': 0,
                'no-match': 0
            }
        },
    ]

    context_api = Context(contexts, session)

    context_api.set('__system_counters__', parameters={})

    assert context_api.get('__system_counters__')['parameters'] == {}
