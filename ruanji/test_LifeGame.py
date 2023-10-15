from unittest import TestCase
from LifeGame import LifeGame
from GameMap import GameMap
from unittest.mock import Mock
import tkinter as tk


class TestLifeGame(TestCase):
    def setUp(self):
        self.life_game = LifeGame(5, 5, 1)

    def test_game_cycle(self):
        self.life_game.game_cycle()
        self.assertEqual([[1, 0, 1],[0, 0, 0],[1, 0, 1]], [row[1:4] for row in self.life_game.mapp.grid[1:4]])

    def test_check_stability(self):
        # Mock the grid_set to contain the current_state
        current_state = tuple(tuple(row) for row in self.life_game.mapp.grid)
        # self.life_game.game_cycle()
        self.life_game.grid_set.add(current_state)

        # # Test if check_stability returns True when the current state is in grid_set
        self.assertTrue(self.life_game.check_stability())

        # Test if check_stability returns False when the current state is not in grid_set
        self.life_game.grid_set.remove(current_state)
        self.assertFalse(self.life_game.check_stability())

    def test_check_stability1(self):
        self.life_game.grid_set.clear()
        self.assertFalse(self.life_game.check_stability())