# Dialogflow Fulfillment Library

## Introduction

A Dialogflow's webhook fulfillment API v2 library for Python.

**Note:** This package currently supports only Dialogflow's API V2 type responses for generic platforms

## Current Features
* Webhook Client
  * Handle requests using a custom fulfillment function or a map of functions for each intent
* Rich Responses
  * Text
  * Quick Replies
* Context API
  * Add/set/delete outgoing contexts from Webhook Client

## Installation
```shell
pip install dialogflow-fulfillment
```

## A Simple Example
```python
from dialogflow_fulfillment import WebhookClient


def handler(agent):
    """Custom handler function"""


# Create a WebhookClient, passing in the request dictionary
agent = WebhookClient(request)

# Handle the request using a handler or map of handlers
agent.handle_request(handler)

# Get the response dictionary
response = agent.response
```

## More Examples
* [Using `dialogflow_fulfillment` in a Flask application](https://github.com/gcaccaos/dialogflow-fulfillment/blob/master/examples/flask/app.py)
* [Using `dialogflow_fulfillment` in a Django view](https://github.com/gcaccaos/dialogflow-fulfillment/blob/master/examples/django/views.py)

## TODO
* Add support for platforms
* Add support for other rich responses
* Add unit tests

## License
See LICENSE.
