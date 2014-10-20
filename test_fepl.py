__author__ = 'Robbie'

from unittest import TestCase
from fantasy_epl import get_soup_object, extract_soup
import player
import fixtures
import start


class TestFEPL(TestCase):

    def setUp(self):
        pass

    def test_get_player_list(self):
        player_list = player.get_players_list()
        self.assertIsNotNone(player_list)
        self.assertIsNot(player_list, [])

    def test_get_fixtures(self):
        home, away = fixtures.get_fixtures(8)
        self.assertIsNotNone(home)
        self.assertIsNotNone(away)

    def test_start(self):
        start.start(7)

    def tearDown(self):
        pass

