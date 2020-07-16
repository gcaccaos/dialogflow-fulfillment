from dialogflow_fulfillment import QuickReplies, WebhookClient


# Define a custom handler function
def handler(agent: WebhookClient) -> None:
    """
    This handler sends a text message along with a quick replies 
    message back to Dialogflow, which uses the messages to build
    the final response to the user.
    """
    agent.add('How are you feeling today?')
    agent.add(QuickReplies(quick_replies=['Happy :)', 'Sad :(']))


# Create an instance of the WebhookClient
agent = WebhookClient(request)

# Handle the request using the handler function
agent.handle_request(handler)
