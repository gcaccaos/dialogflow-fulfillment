from logging import INFO
from typing import Dict

from dialogflow_fulfillment import WebhookClient
from flask import Flask, request
from flask.logging import create_logger

# Create Flask app and enable info level logging
app = Flask(__name__)
logger = create_logger(app)
logger.setLevel(INFO)


def handler(agent: WebhookClient) -> None:
    """Handle the webhook request."""


@app.route('/', methods=['POST'])
def webhook() -> Dict:
    """Handle webhook requests from Dialogflow."""
    # Get WebhookRequest object
    request_ = request.get_json(force=True)

    # Log request headers and body
    logger.info(f'Request headers: {dict(request.headers)}')
    logger.info(f'Request body: {request_}')

    # Handle request
    agent = WebhookClient(request_)
    agent.handle_request(handler)

    # Log WebhookResponse object
    logger.info(f'Response body: {agent.response}')

    return agent.response


if __name__ == '__main__':
    app.run(debug=True)
