# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../kenl380')))

print("PyLib Package {} unittest".format(__file__))
print("PYTHONPATH=")
for item in sys.path:
    print('  {}'.format(item))

import pylib
