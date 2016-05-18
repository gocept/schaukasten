============
Installation
============

Backend
=======

Install ``postgres`` if needed and add a new database::

    $ createdb schaukasten

Setup a virtual environment for this python project::

    $ virtualenv3.5 .
    $ source bin/activate

Install the required packages::

    $ pip install -r requirements.txt

And start by serving the development environment::

    $ pserve development.ini

Frontend
========

Install the ``grunt-cli`` and ``npm`` if not present and just run the following commands to build the frontend::

    $ npm install
    $ grunt
    $ grunt phantomjs

Documentation
=============

To build the documentation install the doc dependencies in your virtualenv and build it::

    $ pip install -r doc-requirements.txt
    $ sphinx-build -b html doc build/doc

Running Tests
=============

To run the tests for frontend with ``grunt`` and for the backend with ``py.test`` simple type::

    $ grunt phantomjs
    $ py.test
