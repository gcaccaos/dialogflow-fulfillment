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
### With Flask
```python
# app.py
from logging import DEBUG

from dialogflow_fulfillment import WebhookClient
from flask import Flask, request
from flask.logging import create_logger

# Create Flask app and enable info level logging
APP = Flask(__name__)
LOG = create_logger(APP)
LOG.setLevel(DEBUG)


def handler(agent):
    """Custom handler function"""


@APP.route('/', methods=['POST'])
def webhook():
    """Handles Dialogflow's webhook requests"""
    # Get request body
    request_ = request.get_json(force=True)

    # Log request headers and body
    LOG.info(f'Request headers: {dict(request.headers)}')
    LOG.info(f'Request body: {request_}')

    # Handle request
    agent = WebhookClient(request_)
    agent.handle_request(handler)

    # Log response body
    LOG.info(f'Response body: {agent.response}')

    return agent.response


if __name__ == '__main__':
    APP.run(debug=True)
```

### With Django
```python
# views.py
from logging import DEBUG, getLogger

from dialogflow_fulfillment import WebhookClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create logger and enable info level logging
LOG = getLogger(__name__)
LOG.setLevel(DEBUG)


def handler(agent):
    """Custom handler function"""


@csrf_exempt
def webhook(request):
    """Handles Dialogflow's webhook requests"""
    if request.method == 'POST':
        # Get request body
        request_ = request.POST.dict()

        # Log request headers and body
        LOG.info(f'Request headers: {dict(request.headers)}')
        LOG.info(f'Request body: {request_}')

        # Handle request
        agent = WebhookClient(request_)
        agent.handle_request(handler)

        # Log response body
        LOG.info(f'Response body: {agent.response}')

        return JsonResponse(agent.response)
```

## TODO
* Add support for platforms
* Add support for other rich responses
* Add unit tests

## License
See LICENSE.
