from json import loads
from logging import getLogger

from dialogflow_fulfillment import WebhookClient
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = getLogger('django.server.webhook')


def handler(agent: WebhookClient) -> None:
    """Handle the webhook request."""


@csrf_exempt
def webhook(request: HttpRequest) -> HttpResponse:
    """Handle webhook requests from Dialogflow."""
    if request.method == 'POST':
        # Get WebhookRequest object
        request_ = loads(request.body)

        # Log request headers and body
        logger.info(f'Request headers: {dict(request.headers)}')
        logger.info(f'Request body: {request_}')

        # Handle request
        agent = WebhookClient(request_)
        agent.handle_request(handler)

        # Log WebhookResponse object
        logger.info(f'Response body: {agent.response}')

        return JsonResponse(agent.response)

    return HttpResponse()
