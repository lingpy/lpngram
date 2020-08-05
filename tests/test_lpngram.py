#!/usr/bin/env python3
# pylint: disable=no-self-use

"""
test_lpngram
============

Tests for the `lpngram` package.
"""

# Import Python libraries
import unittest

# Impor the library itself
import lpngram


class TestLPNgram(unittest.TestCase):
    """
    Suite of tests for the `lpngram` library.
    """

    def test_dummy(self):
        assert 1 == 1


if __name__ == "__main__":
    # Explicitly creating and running a test suite allows to profile it
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLPNgram)
    unittest.TextTestRunner(verbosity=2).run(suite)
