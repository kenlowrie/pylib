# -*- coding: utf-8 -*-

from .context import pylib

import os
import sys
import unittest
import logging

class PyLibPathTests(unittest.TestCase):
    """Various path API test cases for PyLib."""

    def test_ntpx(self):
        cwd = os.getcwd()
        MISSING = 'missing_file'
        MISSING_EXT = 'missing_file.ext'
        EXISTS = 'LICENSE'
        EXISTS_EXT = 'tox.ini'
        n0 = pylib.ntpx(MISSING)
        n1 = pylib.ntpx(MISSING_EXT)
        n2 = pylib.ntpx(EXISTS)
        n3 = pylib.ntpx(EXISTS_EXT)
        
        for n, f in [(n0, MISSING), (n1, MISSING_EXT), (n2, EXISTS), (n3, EXISTS_EXT)]:
            logging.info('Common Testing {}'.format(n.format('dpnx')))
            full, drive, path, name, ext, fsize, ftime = n.all()
            self.assertEqual(full, n.format('dpnx'))
            self.assertFalse(drive)
            self.assertFalse(n.drive())
            self.assertEqual(cwd+os.sep, n.path())
            self.assertEqual(path, n.path())
            fn, fx = os.path.splitext(f)
            self.assertEqual(name, fn)
            self.assertEqual(fn, n.name())
            if fx:
                self.assertEqual(ext, fx)
                self.assertEqual(fx, n.ext())
            else:
                self.assertFalse(ext)
                self.assertFalse(n.ext())

        for n, f in [(n0, MISSING), (n1, MISSING_EXT)]:
            logging.info('No Filesize or Filetime {}'.format(n.format('dpnx')))
            full, drive, path, name, ext, fsize, ftime = n.all()
            self.assertFalse(fsize)
            self.assertFalse(n.size())
            self.assertFalse(ftime)
            self.assertFalse(n.datetime())

        for n, f in [(n2, EXISTS), (n3, EXISTS_EXT)]:
            logging.info('Filesize {} -- Filetime {} for {}'.format(n.size(), n.datetime(), n.format('dpnx')))
            full, drive, path, name, ext, fsize, ftime = n.all()
            self.assertTrue(fsize)
            self.assertTrue(n.size())
            self.assertTrue(ftime)
            self.assertTrue(n.datetime())

    def test_parent(self):
            cwd = os.getcwd()
            while cwd != os.sep:
                logging.info('testing : {}'.format(cwd))
                self.assertTrue(pylib.parent(cwd), os.path.dirname(cwd))
                cwd = pylib.parent(cwd)

    def test_pushd_and_popd(self):
        logging.info('Testing pushd and popd')
        logging.info('Calling pushd() with invalid parameters...')
        with self.assertRaises(TypeError):
            pylib.pushd(5)

        cwd = os.getcwd()
        pylib.pushd()
        self.assertEquals(cwd,os.getcwd())
        pylib.popd()
        self.assertEquals(cwd,os.getcwd())

        logging.info('Calling pushd() with invalid directory...')
        with self.assertRaises(FileNotFoundError):
            pylib.pushd('this_dir_does_not_exist')

        logging.info('Calling pushd() with invalid directory but asking for T/F...')
        self.assertFalse(pylib.pushd('this_dir_does_not_exist', False))

        logging.info('Calling popd() on empty stack')
        with self.assertRaises(ValueError):
            pylib.popd()

        def stack_it_up(just_stack=False):
            cwd = os.getcwd()
            dirs = []
            while cwd != os.sep:
                logging.info('Pushing to: {}'.format(cwd))
                self.assertTrue(pylib.pushd(cwd))
                dirs.append(cwd)
                cwd = pylib.parent(cwd)

            if just_stack:
                return

            logging.info('Okay, now, popping the stack: cwd is {}'.format(os.getcwd()))
            while dirs:
                self.assertEquals(os.getcwd(), dirs.pop())
                self.assertTrue(pylib.popd())
                logging.info('Popped to: {}'.format(os.getcwd()))

        stack_it_up()
        logging.info('Pushing back to root again: cwd is {}'.format(os.getcwd()))
        cwd0 = os.getcwd()
        stack_it_up(True)
        self.assertNotEquals(cwd0,os.getcwd())
        logging.info('Popping all at once: cwd is {}'.format(os.getcwd()))
        pylib.popd(True)
        logging.info('Now back to start: cwd is {}'.format(os.getcwd()))
        self.assertEquals(cwd0,os.getcwd())        
        logging.info('Pop on empty stack: cwd is {}'.format(os.getcwd()))
        with self.assertRaises(ValueError):
            pylib.popd()


if __name__ == '__main__':
    unittest.main()
