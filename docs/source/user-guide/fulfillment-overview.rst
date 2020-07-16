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

    -- Source: `Fulfillment`_.

.. _`Fulfillment`: https://cloud.google.com/dialogflow/docs/fulfillment-overview
