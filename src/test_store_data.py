import unittest
from store_data import Players
from nba_api.stats.static import players


class MyTestCase(unittest.TestCase):
    def test_get_player_name(self):
        # get_player_name = players.get_active_players()
        self.assertIsNotNone(players.get_player_name())


if __name__ == '__main__':
    unittest.main()
