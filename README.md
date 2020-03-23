# Dialogflow Fulfillment Library

[![image](https://img.shields.io/pypi/v/dialogflow-fulfillment.svg)](https://pypi.python.org/pypi/dialogflow-fulfillment)
![image](https://img.shields.io/badge/python-3-blue.svg)

This is an unofficial Dialogflow Fulfillment Package for Python 3.

> When an intent with fulfillment enabled is matched, Dialogflow sends a request to your webhook service with information about the matched intent. Your system can perform any required actions and respond to Dialogflow with information for how to proceed.
>
> -- [*Dialogflow's documentation*](https://cloud.google.com/dialogflow/docs/fulfillment-overview)

**Please notice:** This package currently supports only responses for generic platforms

## Current Features

* Webhook Client
  * Handle requests using a custom handler function or a map of handlers for each intent
* Rich Responses
  * Text
  * Image
  * Quick Replies
  * Payload
* Context API
  * Add/set/delete outgoing contexts from Webhook Client

## Installation

```shell
pip install dialogflow-fulfillment
```

## Quick start

```python
from dialogflow_fulfillment import WebhookClient


def handler(agent):
    """Custom handler function"""


# Create an instance of WebhookClient
agent = WebhookClient(request)

# Handle the request using a handler function or map of handlers
agent.handle_request(handler)

# Get the response dictionary
response = agent.response
```

## Examples

* [Using `dialogflow-fulfillment` in a Flask application](https://github.com/gcaccaos/dialogflow-fulfillment/blob/master/samples/flask/app.py)
* [Using `dialogflow-fulfillment` in a Django view](https://github.com/gcaccaos/dialogflow-fulfillment/blob/master/samples/django/views.py)

## References

* [Dialogflow's WebhookClient class documentation](https://dialogflow.com/docs/reference/fulfillment-library/webhook-client)
* [Dialogflow's RichResponse classes documentation](https://dialogflow.com/docs/reference/fulfillment-library/rich-responses)

## Limitations

* Currently supports responses only for generic platforms

## TODO

* Add support for platforms
* Add support for other rich responses
* Add unit tests

## License

See LICENSE.
