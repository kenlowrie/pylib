# -*- coding: utf-8 -*-

from .context import pylib

import sys
import unittest
#from unittest import TestCase, TestLoader, TextTestRunner

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()
    #suite = TestLoader().loadTestsFromTestCase(BasicTestSuite)
    #TextTestRunner(verbosity=2).run(suite)
