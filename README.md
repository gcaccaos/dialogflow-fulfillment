# dialogflow-fulfillment

![PyPI](https://img.shields.io/pypi/v/dialogflow-fulfillment)
[![Documentation Status](https://readthedocs.org/projects/dialogflow-fulfillment/badge/?version=latest)](https://dialogflow-fulfillment.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/gcaccaos/dialogflow-fulfillment)](https://github.com/gcaccaos/dialogflow-fulfillment/blob/master/LICENSE)

*dialogflow-fulfillment* is a package for Python that helps developers to
create fulfillment webhook services for Dialogflow.

The package provides an API for creating and manipulating response messages,
output contexts and follow-up events in conversations.

## A simple example

```python
from dialogflow_fulfillment import QuickReplies, WebhookClient


# Define a custom handler function
def handler(agent: WebhookClient) -> None:
    """
    This handler sends a text message along with a quick replies message
    back to Dialogflow, which uses the messages to build the final response
    to the user.
    """
    agent.add('How are you feeling today?')
    agent.add(QuickReplies(quick_replies=['Happy :)', 'Sad :(']))


# Create an instance of the WebhookClient
agent = WebhookClient(request)

# Handle the request using the handler function
agent.handle_request(handler)

# Get the response
response = agent.response
```

## Installation

The preferred way to install *dialogflow-fulfillment* is from
[PyPI](https://pypi.org/project/dialogflow-fulfillment/) with
[**pip**](https://pip.pypa.io/):

```shell
pip install dialogflow-fulfillment
```

## Features

*dialogflow-fulfillment*'s key features are:

* **Webhook Client**: handle webhook requests using a custom handler function
  or a map of handlers for each intent
* **Contexts**: process input contexts and add, set or delete output contexts
* **Events**: trigger follow-up events with optional parameters
* **Rich Responses**: create and send the following types of rich response
  messages:
  * Text
  * Image
  * Card
  * Quick Replies
  * Payload

## More examples

* [Dialogflow fulfillment webhook server with **Flask**](https://dialogflow-fulfillment.readthedocs.io/en/latest/getting-started/examples/flask/)
* [Dialogflow fulfillment webhook server with **Django**](https://dialogflow-fulfillment.readthedocs.io/en/latest/getting-started/examples/django/)

## Documentation

For more information about the package, guides and examples of usage, see the
[documentation](https://dialogflow-fulfillment.readthedocs.io).

## Contribute

All kinds of contributions are welcome!

For an overview about how to contribute to *dialogflow-fulfillment*, see the
[contributing guide](CONTRIBUTING.rst).

## License

This project is licensed under the Apache 2.0 license.

For more details about the license, see the [LICENSE file](LICENSE).

## Acknowledgments

Thanks to the Dialogflow development team!
