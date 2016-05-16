from alex_pypi_test import Echoer
import unittest

class TestEchoer(unittest.TestCase):
    """
    Simple class to test Echoer class
    """

    def test_echoer(self):
        """
        Simple method to test the echo method in Echoer class
        :return: None
        """
        e = Echoer()
        e.echo("Alex")


if __name__ == '__main__':
    unittest.main()