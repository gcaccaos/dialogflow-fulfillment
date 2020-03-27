# Dialogflow Fulfillment Library

---

![PyPI](https://img.shields.io/pypi/v/dialogflow-fulfillment)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dialogflow-fulfillment?label=pypi%20downloads)
[![Documentation Status](https://readthedocs.org/projects/dialogflow-fulfillment/badge/?version=latest)](https://dialogflow-fulfillment.readthedocs.io/en/latest/?badge=latest)
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

## Installing

### Via `pip`

`dialogflow-fulfillment` is available for download from PyPI via `pip`:

```shell
pip install dialogflow-fulfillment
```

### From source

To install `dialogflow-fulfillment` from source, clone this repository and run `setup.py install` from the project's root directory:

```shell
git clone https://github.com/gcaccaos/dialogflow-fulfillment.git
cd dialogflow-fulfillment
python setup.py install
```

### For development

The package can be installed from source with `pip` in __editable mode__ or with `setup.py` in __development mode__, which means that there's no need to install from source after every change in the code.

```shell
git clone https://github.com/gcaccaos/dialogflow-fulfillment.git
cd dialogflow-fulfillment

pip install -e .

# or

python setup.py develop
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

## Documentation

* [`dialogflow-fulfillment` documentation](https://dialogflow-fulfillment.readthedocs.io)

## Testing

Tests for this package are written with `unittest` and managed by `tox`.

The `tox.ini` file at the project's root directory is used for configuring the tests.

To run the tests, clone this repository, install `tox` via `pip` and run `tox` command from the project's root directory:

```shell
git clone https://github.com/gcaccaos/dialogflow-fulfillment.git
pip install tox
cd dialogflow-fulfillment
tox
```

## Limitations

* Currently supports responses only for generic platforms

## TODO

* Add support for platforms
* Add support for other rich responses
* Add unit tests
* Add documentation

## License

See LICENSE.

## Acknowledgments

* Dialogflow team
