import time
import threading

class GameTimer(object):
    def __init__(self, trigger, interval):
        """将在主程序中初始化实例，计时器以interval秒的频率触发
        trigger是个函数，计时器被触发时调用该函数"""
        self.trigger = trigger
        self.interval = interval
        self._running = False
        self._timer = None

    def _run(self):
        while self._running:
            self.trigger()  # 调用触发函数
            time.sleep(self.interval)

    def start(self):
        """启动计时器，之后将以interval秒的间隔持续触发"""
        if not self._running:
            self._running = True
            self._timer = threading.Thread(target=self._run)
            self._timer.start()

    def stop(self):
        """停止计时器"""
        self._running = False
        if self._timer:
            self._timer.join()
