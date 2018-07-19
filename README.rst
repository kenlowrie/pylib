ken380l.pylib
=============

.. image:: https://travis-ci.org/kenlowrie/pylib.svg?branch=add%2Fdocs_and_unittests
    :target: https://travis-ci.org/kenlowrie/pylib

PyLib is a library of useful (to me) functions and classes for building
applications and packages written in Python. It supports both 2.x and 3.x
versions of Python.

Installing
^^^^^^^^^^

::

    pip install kenl380.pylib

Credits
^^^^^^^

PyLib was written and is maintained by 
`Ken Lowrie <https://github.com/kenlowrie>`__

License
^^^^^^^

PyLib is released under the 
`Apache 2.0 license <https://opensource.org/licenses/Apache-2.0>`__


Developing
^^^^^^^^^^

Set up environment using pipenv:

::

    pipenv install  # only required once to setup the virtual environment
    pipenv shell
    # need to think through how this should work.
    pip install -e .

After this, the `import kenl380.pylib` command will use the working copy of your code.

To run unit tests and style checks, run this command from your pipenv shell:

::

    tox
