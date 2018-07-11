# -*- coding: utf-8 -*-

from .context import pylib

import sys
import unittest
import logging

ALIAS = '__alias__'

class PyLibContextTests(unittest.TestCase):
    """Basic test cases."""

    def whoami(self):
        """returns a string indicating who i am."""

        try:
            myself = __file__
        except NameError:
            myself = argv[0]

        return myself

    def expectations(self):
        from os.path import abspath, split, splitext

        who_am_i = abspath(self.whoami())
        where_am_i, script_name = split(who_am_i)
        
        default_alias, ext = splitext(script_name)

        return (who_am_i, where_am_i, default_alias)

    def py_version_str(self):
        from sys import version_info

        return "Python Interpreter Version: {}.{}.{}".format(version_info.major,
                                                             version_info.minor,
                                                             version_info.micro)

    def test_globals(self):
        logging.info("testing globals from pylib")

        logging.info("user: [{}]".format(pylib.USER))
        logging.info("computer: [{}]".format(pylib.COMPUTER))
        logging.info("tempdir: [{}]".format(pylib.TEMPDIR))

        self.assertTrue(pylib.USER)
        self.assertTrue(pylib.COMPUTER)
        self.assertTrue(pylib.TEMPDIR)

    def test_context(self):
        logging.info("testing context class")

        with self.assertRaises(TypeError):
            pylib.context()

        who, where, def_alias = self.expectations()

        logging.info("expectations: [{}][{}][{}]".format(who, where, def_alias))

        me0 = pylib.context(self.whoami())
        me1 = pylib.context(self.whoami(),ALIAS)
        pvs = self.py_version_str()

        for me in [me0, me1]:
            logging.info("me?: [{}][{}][{}]".format(me.whoami(), me.whereami(), me.alias()))
            self.assertEquals(me.whoami(), who)
            self.assertEquals(me.whereami(), where)
            self.assertEquals(me.pyVersionStr(), pvs)

        self.assertEquals(me0.alias(), def_alias)
        self.assertEquals(me1.alias(), ALIAS)

        logging.info("pyVersionStr0: [{}]".format(me0.pyVersionStr()))
        logging.info("pyVersionStr1: [{}]".format(me1.pyVersionStr()))
        logging.info("vExpectations: [{}]".format(pvs))

if __name__ == '__main__':
    unittest.main()
