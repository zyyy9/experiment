import time
import threading

class GameTimer(object):
    def __init__(self, trigger, interval):
        """将在主程序中初始化实例，计时器以interval秒的频率触发
        trigger是个函数，计时器被触发时调用该函数"""
        self.trigger = trigger
        self.interval = interval
        self.running = False  # 用于跟踪游戏是否在运行
        self.stop_flag = threading.Event()
        self.timer = None

    def start(self):
        """启动计时器，之后将以interval秒的间隔持续触发"""
        self.timer = threading.Thread(target=self._timer_thread)
        self.stop_flag = threading.Event()
        if self.running:
            self.timer.start()

    def _timer_thread(self):
        """计时器线程的主要逻辑"""
        while not self.stop_flag.is_set():
            self.trigger()  # 调用触发函数
            time.sleep(self.interval)  # 等待一段时间

    def stop(self):
        """停止计时器"""
        self.stop_flag.set()
        self.running = False
      #  self.timer = None  # 重置计时器线程
