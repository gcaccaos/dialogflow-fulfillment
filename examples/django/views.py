from logging import DEBUG, getLogger
from typing import Dict

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dialogflow_fulfillment import WebhookClient

# Create logger and enable info level logging
logger = getLogger(__name__)
logger.setLevel(DEBUG)


def handler(agent: WebhookClient) -> None:
    """Handle the webhook request."""


@csrf_exempt
def webhook(request: Dict) -> Dict:
    """Handle webhook requests from Dialogflow."""
    if request.method == 'POST':
        # Get request body
        request_ = request.POST.dict()

        # Log request headers and body
        logger.info(f'Request headers: {dict(request.headers)}')
        logger.info(f'Request body: {request_}')

        # Handle request
        agent = WebhookClient(request_)
        agent.handle_request(handler)

        # Log response body
        logger.info(f'Response body: {agent.response}')

        return JsonResponse(agent.response)
