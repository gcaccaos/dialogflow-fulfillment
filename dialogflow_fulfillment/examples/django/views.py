from logging import DEBUG, getLogger

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dialogflow_fulfillment import WebhookClient

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
