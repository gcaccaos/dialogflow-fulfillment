.. _fulfillment-overview:

Fulfillment overview
====================

What is fulfillment?
--------------------

Dialogflow's console allows to create simple and static responses for user's
intents in conversations. In order to create more dynamic and complex
responses, such as retrieving information from other services, the intent's
**fulfillment setting** must be enabled and a webhook service must be provided:

   When an intent with fulfillment enabled is matched, Dialogflow sends a
   request to your webhook service with information about the matched intent.
   Your system can perform any required actions and respond to Dialogflow with
   information for how to proceed.

   -- Source: Fulfillment_.

.. _Fulfillment: https://cloud.google.com/dialogflow/docs/fulfillment-overview

A detailed example
------------------

.. mermaid::
   :caption: A representation of how data flows in a conversation between a
      user and a Dialogflow agent.

   sequenceDiagram
      autonumber
      User->>+Interface: User query
      Interface->>+Dialogflow: detectIntent request
      Dialogflow->>+Webhook service: WebhookRequest
      Webhook service->>+External API: API query
      External API->>-Webhook service: API response
      Webhook service->>-Dialogflow: WebhookResponse
      Dialogflow->>-Interface: DetectIntentResponse
      Interface->>-User: Display message(s)

The above diagram is a simplified representation of how data flows in a
conversation between a user and a Dialogflow agent through an user interface.
In this example, the user's intent is fulfilled by the agent with the help of
a webhook service, allowing to handle more dynamic responses, like calling an
external API to fetch some information.

Generally, the flow of data in a conversation with fulfillment can be described
(in a simplified way) as follows:

1. The user types a text into the application's front-end in order to send a
   query to the agent.
2. The input is captured by the application's back-end, which calls Dialogflow
   API's :obj:`detectIntent` resource, either via the official client or via
   HTTPS request in the form of a JSON. The request's body contain a
   :obj:`QueryInput` object, which holds the user's query (along with other
   information).
3. Dialogflow detects the intent that corresponds to the user's query and,
   since the intent in this example has the fulfillment setting enabled, posts
   a :obj:`WebhookRequest` object to the external webhook service via HTTPS in
   the form of a JSON. This object has a :obj:`QueryResult` object, which also
   holds the user's query and information about the detected intent, such as
   the corresponding action, detected entities and input or output contexts.
4. The webhook service uses information from the :obj:`QueryResult` object
   (along with other data from the :obj:`WebhookRequest` object) in order to
   determine how the conversation must go. For example, it could trigger some
   event by setting an :obj:`EventInput`, change the value of a parameter in a
   :obj:`Context` or generate :obj:`Message` objects using data from external
   services, such as APIs or databases.
5. In this example, the webhook service calls an external API in order to
   fulfill the user's query.
6. Then, a :obj:`WebhookResponse` object with the generated response data is
   returned to Dialogflow.
7. Dialogflow validates the response, checking for present keys and value
   types, and returns a :obj:`DetectIntentResponse` object to the interface
   application.
8. Finally, the application's front-end displays the resulting response
   message(s) to the user.
