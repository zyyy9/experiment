import unittest
from unittest import TestCase
from LifeGame import LifeGame
from unittest.mock import patch


class TestLifeGame(TestCase):
    def setUp(self):
        self.life_game = LifeGame(5, 5, 0)

    def test_game_cycle(self):
        for i in range(1, 4):
            self.life_game.mapp.grid[2][i] = 1
        self.life_game.grid_set.add(tuple(tuple(row) for row in self.life_game.mapp.grid))
        self.life_game.game_timer.running = True
        self.life_game.game_cycle()
        self.assertEqual([[0, 1, 0], [0, 1, 0], [0, 1, 0]], [row[1:4] for row in self.life_game.mapp.grid[1:4]])

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

    def test_start_game(self):
        with patch.object(self.life_game.game_timer, "trigger") as trigger_mock:
            self.life_game.start_game()
            self.assertTrue(self.life_game.game_timer.running)
            self.life_game.game_timer.stop()
            self.assertEqual(self.life_game.start_button["state"], "disabled")
            self.assertEqual(self.life_game.pause_button["state"], "normal")
            self.assertEqual(self.life_game.reset_button["state"], "normal")

    def test_pause_game(self):
        self.life_game.pause_game()
        self.assertFalse(self.life_game.game_timer.running)
        self.assertEqual(self.life_game.start_button["state"], "normal")
        self.assertEqual(self.life_game.pause_button["state"], "disabled")
        self.assertEqual(self.life_game.reset_button["state"], "normal")

    def test_reset_game(self):
        self.life_game.reset_game()
        self.assertFalse(self.life_game.game_timer.running)
        self.assertEqual(self.life_game.start_button["state"], "normal")
        self.assertEqual(self.life_game.pause_button["state"], "disabled")
        self.assertEqual(self.life_game.reset_button["state"], "disabled")

if __name__ == '__main__':
    unittest.main()