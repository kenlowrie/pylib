===================
PyLib API Reference
===================

:author: Ken Lowrie

:mod:`pylib` --- aka kenl380.pylib
----------------------------------

.. automodule:: pylib

pylib Module-wide data
----------------------

Yes, module-wide data is another way of saying Global (ugh) variables. 
In the current version, there are three (3) of them.

.. autodata:: USER
    :annotation: - `str` object
    
.. autodata:: COMPUTER
    :annotation:  - `str` object

.. autodata:: TEMPDIR
    :annotation:  - `str` object

pylib.context Class
-------------------

The context class provides a quick way to get at some useful information
about the current module.

.. autoclass:: pylib.context
    :members:

pylib.ntpx Class
----------------

The `pylib.ntpx` class will probably be deprecated soon. Python 3's :mod:`pathlib`
is more flexible and has much more support. At the very least, I should refactor
`ntpx` to use :mod:`pathlib` if running on 3.x.

.. autoclass:: pylib.ntpx
    :members:

pylib methods
-------------

.. autofunction:: pylib.parent

.. autofunction:: pushd

.. autofunction:: popd

