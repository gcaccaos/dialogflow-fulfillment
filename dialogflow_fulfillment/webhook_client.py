class WebhookClient:
    def __init__(self, request, response=None, handler=None):
        self.request = request
        self.response = response
        self.handler = handler

    def handle_request(self):
        self.response = self.handler(self.request)
