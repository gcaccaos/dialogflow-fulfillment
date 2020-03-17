from logging import DEBUG

from flask import Flask, request
from flask.logging import create_logger

from dialogflow_fulfillment import WebhookClient

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
