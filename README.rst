pylib
=====

.. image:: https://travis-ci.org/kenlowrie/pylib.svg?branch=add%2Fdocs_and_unittests
    :target: https://travis-ci.org/kenlowrie/pylib

PyLib is a library of useful (to me) functions and classes for building
applications and packages written in Python. It supports both the 2.x and 3.x
versions of Python.

Installing
^^^^^^^^^^

::

    pip install kenl380.pylib

Documentation
^^^^^^^^^^^^^

Read the documentation for PyLib. (TODO: hyperlink this to online docs)

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

Start by setting up your environment using pipenv. Switch to the local
copy of your repository and:

::

    pipenv install

The ``pipenv install`` step is only required once to setup the virtual
environment. After that, you can type ``pipenv shell`` to spawn a shell
that's setup for working on pylib. You will probably want to install
pylib in develop or edit mode, so:

::

    pipenv shell
    pip install -e .

And you're all set. If you're building an application, you can:

::

    import kenl380.pylib as pylib

to load the methods and classes from ``pylib`` into your applications'
namespace.

Make sure that you write unittests for any new methods or classes that you
add. You can test them using ``tox``.

For example, to run unit tests, issue this command from your pipenv shell:

::

    tox

Conclusion
^^^^^^^^^^

If you have questions or comments, feel free to message me or email me. If
you find an issue, please add it to GitHub.
