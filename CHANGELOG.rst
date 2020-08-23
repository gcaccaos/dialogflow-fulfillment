Change log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_ and this project adheres to
`Semantic Versioning`_.

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

0.3.0_ - 2020-07-29
------------------

Added
~~~~~

* Docs: Add change log and contributing guide.
* Small improvements to the classes and methods docstrings.
* set_text() method for the Text response.
* set_subtitle(), set_image() and set_buttons() methods for the Card response.
* set_title() and set_quick_replies() to the QuickReplies response.

Fixed
~~~~~

* Fix Card and QuickReply missing fields.
* Fix optional parameters for all rich responses.
* Fix WebhookClient's parsing of Image and Card responses.
* Fix RichResponse instantiation (shouldn't be able to instantiate an abstract
  base class).

Changed
~~~~~~~

* Docs: Change theme to Read the Docs' theme.

0.2.0_ - 2020-07-17
------------------

Added
~~~~~

* Tests for Context and WebhookClient.

Changed
~~~~~~~

* Refactored tests to use pytest.

0.1.5_ - 2020-07-17
------------------

Fixed
~~~~~

* Fix bug in WebhookClient's key access in _process_request().

0.1.4_ - 2020-07-17
------------------

Added
~~~~~

* Type hints for WebhookClient methods.
* Type hints for Context methods.
* Type hints for RichResponse methods.

Changed
~~~~~~~

* Refactor WebhookClient's key access in _process_request().

0.1.3_ - 2020-07-17
------------------

Added
~~~~~

* Package's public API.

0.1.2_ - 2020-03-27
------------------

* First release.

.. _0.3.0: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.2.0...v0.3.0
.. _0.2.0: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.5...v0.2.0
.. _0.1.5: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.4...v0.1.5
.. _0.1.4: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.3...v0.1.4
.. _0.1.3: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.2...v0.1.3
.. _0.1.2: https://github.com/gcaccaos/dialogflow-fulfillment/releases/tag/v0.1.2
