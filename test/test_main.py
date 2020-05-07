#!/usr/bin/python
""" test_main

Author: datadonk23
Date: 07.05.20 
"""

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
