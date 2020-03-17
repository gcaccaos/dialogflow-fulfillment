# dialogflow-fulfillment-python

## Introduction

A Dialogflow's webhook fulfillment API v2 library for Python.

Currently, this library handles responses only for generic platforms and is 
meant to be used only for API v2 responses. 

### TODO List
* Add support for all platforms
* Add support for other rich responses

## Current Features
* Webhook Client
  * Handle requests using a custom fulfillment function or a map of functions for each intent
* Rich Responses
  * Text
  * Quick Replies

## Installation
### For development
```shell
cd dialogflow-fulfillment-python
pip install -e .
```

## Usage
### General
```python
from dialogflow_fulfillment import WebhookClient


# Create a WebhookClient, passing in the request dictionary
agent = WebhookClient(request)

# Handle the request using a handler or map of handlers
agent.handle_request(handler)

# Get the response dictionary
response = agent.response
```

### With Flask
```python
from dialogflow_fulfillment import WebhookClient
from flask import Flask, request

# Import custom handler
from my_handler import handler


APP = Flask(__name__)

@APP.route('/', methods=['POST'])
def webhook():
    request_ = request.get_json(force=True)

    agent = WebhookClient(request_)
    agent.handle_request(handler)

    return agent.response


if __name__ == '__main__':
    APP.run(debug=True)

```