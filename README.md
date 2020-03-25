# Dialogflow Fulfillment Library

---

![PyPI](https://img.shields.io/pypi/v/dialogflow-fulfillment)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dialogflow-fulfillment?label=pypi%20downloads)
[![GitHub license](https://img.shields.io/github/license/gcaccaos/dialogflow-fulfillment)](https://github.com/gcaccaos/dialogflow-fulfillment/blob/master/LICENSE)

This is an unofficial Dialogflow Fulfillment package for Python 3+.

This package can be used to manipulate or create messages, output contexts and followup events for a matched intent.

> When an intent with fulfillment enabled is matched, Dialogflow sends a request to your webhook service with information about the matched intent. Your system can perform any required actions and respond to Dialogflow with information for how to proceed.
>
> -- [*Dialogflow's documentation*](https://cloud.google.com/dialogflow/docs/fulfillment-overview)

**Please notice:** this package currently supports only responses for generic platforms

## Features

* Webhook Client
  * Handle requests using a custom handler function or a map of handlers for each intent
* Rich Responses
  * Text
  * Image
  * Card
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
* Add documentation

## License

See LICENSE.
