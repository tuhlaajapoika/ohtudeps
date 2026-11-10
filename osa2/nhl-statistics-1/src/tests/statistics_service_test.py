import unittest

from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_name_kurri(self):
        player = self.stats.search("Kurri")
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_search_missing_name(self):
        self.assertIs(self.stats.search("zzz"), None)

    def test_team_get_edm(self):
        expected = ["Semenko", "Kurri", "Gretzky"]
        names = []
        for player in self.stats.team("EDM"):
            names.append(player.name)
        self.assertListEqual(expected, names)

    def test_top_three(self):
        expected = ["Gretzky", "Lemieux", "Yzerman"]
        names = []
        # top logic: "how many indexes" (0,1,2)
        for player in self.stats.top(2):
            names.append(player.name)
        self.assertListEqual(expected, names)
