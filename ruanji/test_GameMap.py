from unittest import TestCase
from GameMap import GameMap


class TestGameMap(TestCase):
    def setUp(self):
        self.game_map = GameMap(10, 10)

    def test_reset(self):

        # 测试重置后的地图是否有活细胞存在
        self.game_map.reset(0.3)
        live_cells = sum(row.count(1) for row in self.game_map.grid)
        self.assertTrue(live_cells > 0)

        # 测试重置后的地图是否没有活细胞存在
        self.game_map.reset(0.0)
        live_cells = sum(row.count(1) for row in self.game_map.grid)
        self.assertEqual(live_cells, 0)

        # 测试重置后的地图是否都是活细胞
        self.game_map.reset(1.0)
        live_cells = sum(row.count(1) for row in self.game_map.grid)
        self.assertEqual(live_cells, 64)

    def test_get_set(self):
        self.assertEqual(0, self.game_map.get(0, 1))
        self.game_map.set(0, 1, 1)
        self.assertEqual(1, self.game_map.get(0, 1))

    def test_get_neighbor_count(self):
        expected_value = [[8] * 5] * 5
        self.game_map.grid = [[1] * 5] * 5
        for i in range(1, 4):
            for j in range(1, 4):
                self.assertEqual(expected_value[i][j], (self.game_map.get_neighbor_count(i ,j)), '(%d, %d)'%(i ,j))

