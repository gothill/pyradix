=======
pyradix - A lightweight Python client and CLI for Radix DLT.
=======


.. image:: https://img.shields.io/pypi/v/pyradix.svg
        :target: https://pypi.python.org/pypi/pyradix

.. image:: https://img.shields.io/travis/gothill/pyradix.svg
        :target: https://travis-ci.com/gothill/pyradix

.. image:: https://readthedocs.org/projects/pyradix/badge/?version=latest
        :target: https://pyradix.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


**pyradix** is a Python package for interfacing with the Radix DLT network.

Experimental - use at your own risk!

Installation
==========

::

    $ pip install -U pyradix-dlt


Client
==========

.. code-block:: python

    >>> from pyradix import Client
    >>> client = Client(node_url='https://betanet.radixdlt.com/rpc')
    >>> client.get_token_balances('brx1qsp2kpg432d4ux93mdmjd8wtxpthyrt2ezzy3msupjmahwq5qdt5t8qwmf6k4')
    [
        {
            "amount": "70000000000000000000",
            "rri": "cerb_rb1qvvm3mx58augl027sfv229f6qmsqq6xc7nqkncacxe0sp6faqs",
        },
        {
            "amount": "105000000000000000000",
            "rri": "emunie_rb1q0wsjfurhlus3dz9qgxd84an53cseqcjvl08sv3gr2qqmzkd2c",
        },
        {
            "amount": "97111111200000000000",
            "rri": "gum_rb1qduv0q8xtvgz5jqt4cmedyvaen88hu3pxrchhvp8xx9s5yjeh5",
        },
        {
            "amount": "139706666666666670000",
            "rri": "xrd_rb1qya85pwq"
        },
    ]

* Unofficial project
* Betanet only
* Free software: MIT license
* Learn more about Radix: https://www.radixdlt.com


Coming Soon
==========

* Wallet
* Documentation


TODO:
* CLI
    * Use Click
    * Entry point
* Tests
    * Fix pagination tests
    * Check dummy data
    * Error handling
    * Check call args
* Documentation
    * Expand README
    * Docstrings
* Type hints
* Lint
    * isort
