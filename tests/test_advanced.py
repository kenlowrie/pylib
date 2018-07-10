# -*- coding: utf-8 -*-

from .context import pylib

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNotNone(pylib.context(''))


if __name__ == '__main__':
    unittest.main()
