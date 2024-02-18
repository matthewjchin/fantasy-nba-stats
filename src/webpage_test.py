import unittest

from app import main


class MyTestCase(unittest.TestCase):

    def test_main(self):
        self.assertIs(not None, self)

    def test_echo_input(self):
        self.assertEqual(not None, self)

    def test_get_player_name_active(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
