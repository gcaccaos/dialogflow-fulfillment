Overview
========

.. toctree::
   :hidden:

   getting-started/index
   user-guide/index
   api/index

*dialogflow-fulfillment* is a package for Python that helps developers to
create fulfillment webhook services for Dialogflow.

The package provides an API for creating and manipulating response messages,
output contexts and follow-up events in conversations.

.. seealso::

   For more information about fulfillment and how it works, see
   :ref:`fulfillment-overview`.

A simple example
----------------

Working with *dialogflow-fulfillment* is as simple as passing a request object
from Dialogflow (a.k.a. `WebhookRequest`) to a :class:`~.WebhookClient` and
calling it's :meth:`~.WebhookClient.handle_request` method on a handler
function (or a mapping of functions for each intent):

.. literalinclude:: ../../examples/simple_example.py
   :language: python
   :caption: simple_example.py

The above code produces the resulting response object (a.k.a. `WebhookResponse`):

.. code-block:: python

   >>> agent.response
   {
      'fulfillmentMessages': [
         {
               'text': {
                  'text': [
                     'How are you feeling today?'
                  ]
               }
         },
         {
               'quickReplies': {
                  'quickReplies': [
                     'Happy :)',
                     'Sad :('
                  ]
               }
         }
      ]
   }

Installation
------------

The preferred way to install *dialogflow-fulfillment* is from
`PyPI`_ with `pip`_:

.. code-block:: console

   pip install dialogflow-fulfillment

.. _PyPI: https://pypi.org/project/dialogflow-fulfillment/
.. _pip: https://pip.pypa.io/

.. seealso::

   For further details about the installation, see :ref:`installation`.

Features
--------

*dialogflow-fulfillment*'s key features are:

* **Webhook Client**: handle webhook requests using a custom handler function
  or a map of handlers for each intent
* **Contexts**: process input contexts and add, set or delete output contexts
  in conversations
* **Events**: trigger follow-up events with optional parameters
* **Rich Responses**: create and send the following types of rich response
  messages:

  * Text
  * Image
  * Card
  * Quick Replies
  * Payload

.. seealso::

   For more information, see :ref:`user-guide` and :ref:`api-reference`.

Limitations
-----------

Currently, *dialogflow-fulfillment* has some drawbacks, which will be addressed
in the future:

* No support for platform-specific responses
* Partial code coverage
