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

    $ pip install kenl380.pylib

Documentation
^^^^^^^^^^^^^

Read the documentation for PyLib. It is hosted online at 
`kenl380pylib.readthedocs.io <https://kenl380pylib.readthedocs.io>`__


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

    $ pipenv install

The ``pipenv install`` step is only required once to setup the virtual
environment. After that, you can type ``pipenv shell`` to spawn a shell
that's setup for working on pylib.

`pylib` is installed in edit mode after running the `pipenv install`, so
you can make changes directly to the code and test them interactively
when working inside the `pipenv shell` prompt.

If you're building an application, you can:

::

    import kenl380.pylib as pylib

to load the methods and classes from ``pylib`` into your applications'
namespace.

Update the Docs!
^^^^^^^^^^^^^^^^

Sphinx is used to create the documentation for ``pylib``. Be sure to
add or update the docs for any changes you make. This is required if
you plan on submitting a pull request.

Testing
^^^^^^^

Make sure that you write unittests for any new methods or classes that you
add. You can test them using ``tox``.

For example, to run unit tests, issue this command from your pipenv shell:

::

    $ pipenv shell
    $ tox

PyLib's tox.ini is configured to run all of the unittests on both Python 
2.7 and 3.6, so you need to have both installed locally in order to run
the tests. You can use Homebrew or Pyenv to get multiple versions installed 
on your local system.

Conclusion
^^^^^^^^^^

If you have questions or comments, feel free to 
`contact me via email <mailto:ken@kenlowrie.com>`__. 
If you find an issue, please add it to 
`GitHub <https://github.com/kenlowrie/pylib/issues>`__.
