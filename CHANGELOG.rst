Change log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_ and this project adheres to
`Semantic Versioning`_.

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

0.2.0 - 2020-07-17
------------------

Added
~~~~~

* Tests for Context and WebhookClient.

Changed
~~~~~~~

* Refactored tests to use pytest.

0.1.5 - 2020-07-17
------------------

Bug fixes
~~~~~~~~~

* Fix bug in WebhookClient's key access in _process_request().

0.1.4 - 2020-07-17
------------------

Added
~~~~~

* Type hints for WebhookClient methods.
* Type hints for Context methods.
* Type hints for RichResponse methods.

Changed
~~~~~~~

* Refactor WebhookClient's key access in _process_request().

0.1.3 - 2020-07-17
------------------

Added
~~~~~

* Package's public API.

0.1.2 - 2020-03-27
------------------

* First release.
