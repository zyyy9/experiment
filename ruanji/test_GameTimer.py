from unittest import TestCase
from GameTimer import GameTimer
from LifeGame import LifeGame
from unittest.mock import patch
import threading
import time


class TestGameTimer(TestCase):
    def setUp(self):
        self.life_game = LifeGame(5, 5, 1)
        self.time_r = GameTimer(self.life_game.game_cycle, 0.3)

    def test_start(self):
        # 测试start方法的行为
        # 在这里你可以模拟计时器的运行，并检查它是否启动了线程
        with patch.object(self.time_r, "trigger") as trigger_mock:
            self.time_r.running = True
            self.time_r.start()
            # 在这里可以添加断言来验证计时器是否在运行
            self.assertTrue(self.time_r.timer.is_alive())
            self.time_r.stop()

    def test_stop(self):
        with patch.object(self.time_r, "trigger") as trigger_mock:
            self.time_r.timer = threading.Thread(target=self.time_r._timer_thread)
            self.stop_flag = threading.Event()
            self.time_r.timer.start()
            self.time_r.stop()
            time.sleep(1)
            self.assertFalse(self.time_r.timer.is_alive())
