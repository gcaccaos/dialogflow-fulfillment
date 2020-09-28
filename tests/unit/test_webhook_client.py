import pytest

from dialogflow_fulfillment import WebhookClient


def test_non_dict():
    with pytest.raises(TypeError):
        WebhookClient('this is not a dict')


def test_non_callable_handler(webhook_request):
    agent = WebhookClient(webhook_request)

    handler = 'this is not a callable'

    with pytest.raises(TypeError):
        agent.handle_request(handler)
