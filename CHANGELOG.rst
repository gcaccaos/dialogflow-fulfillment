Change log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_ and this project adheres to
`Semantic Versioning`_.

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

Unreleased
----------

Removed
~~~~~~~

* RichResponse's set_* methods (use property attributes instead).
* WebhookClient's set_followup_event method (use property attribute instead).

0.4.1_ - 2020-10-11
-------------------

Added
~~~~~

* Continuous integration and continuous deployment with Github Actions.

Improved
~~~~~~~~

* Health of the source code.
* Documentation.

0.4.0_ - 2020-09-12
-------------------

Added
~~~~~

* Getters and setters for RichResponse's attributes (and deprecation warnings
  to set_*() methods).
* Getter and setter for WebhookClient's followup_event attribute (and
  deprecation warning to set_followup_event() method).
* Docs: Examples to WebhookClient's methods docstrings.
* Docs: Examples to RichResponse's attributes docstrings.
* Docs: "See also" sections in RichResponse's docstrings.
* Docs: Type hints to WebhookClient's handle_request() method's docstring.
* Docs: "Detailed example" section in "Fulfillment overview" page.

Improved
~~~~~~~~

* Typing annotations coverage.

0.3.0_ - 2020-07-29
-------------------

Added
~~~~~

* Docs: Change log and contributing guide pages.
* set_text() method for the Text response.
* set_subtitle(), set_image() and set_buttons() methods for the Card response.
* set_title() and set_quick_replies() to the QuickReplies response.

Fixed
~~~~~

* Fix missing fields in Card and QuickReply responses.
* Fix optional parameters for all rich responses.
* Fix parsing of Image and Card responses from requests.
* Fix RichResponse instantiation (shouldn't be able to instantiate an abstract
  base class).

Improved
~~~~~~~~
* Docs: improve classes and methods docstrings.

Changed
~~~~~~~

* Docs: Change theme to Read the Docs' theme.

0.2.0_ - 2020-07-17
-------------------

Added
~~~~~

* Tests for Context and WebhookClient.

Changed
~~~~~~~

* Rewrite tests using pytest.

0.1.5_ - 2020-07-17
-------------------

Fixed
~~~~~

* Fix a key access error in WebhookClient's request processing.

0.1.4_ - 2020-07-17
-------------------

Added
~~~~~

* Type hints for WebhookClient methods.
* Type hints for Context methods.
* Type hints for RichResponse methods.

0.1.3_ - 2020-07-17
-------------------

Added
~~~~~

* Public API of the package.

0.1.2_ - 2020-03-27
-------------------

* Initial release.

.. _0.4.1: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.4.0...v0.4.1
.. _0.4.0: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.3.0...v0.4.0
.. _0.3.0: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.2.0...v0.3.0
.. _0.2.0: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.5...v0.2.0
.. _0.1.5: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.4...v0.1.5
.. _0.1.4: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.3...v0.1.4
.. _0.1.3: https://github.com/gcaccaos/dialogflow-fulfillment/compare/v0.1.2...v0.1.3
.. _0.1.2: https://github.com/gcaccaos/dialogflow-fulfillment/releases/tag/v0.1.2
