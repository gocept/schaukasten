=================
API-Documentation
=================

The current RESTfull-API version is 0.1 and allows the following commands.

``/api/``
=========

.. http:get:: /api/

    When successful returns the current version.

    :return:

    .. code-block:: javascript

        {
            "status": "success",
            "version": 0.1,
            "msg": "message describing the current version"
        }

``/files/``
===========

.. http:post:: /files/

    Create a new file.

    :param str filename: The filename of the uploaded file with extension.
    :param str file: The content of the file.

    :return:

    .. code-block:: javascript

        {
            "status": "success",
            "filename": "example.txt",
            "file": "uuid of file entry"
        }


