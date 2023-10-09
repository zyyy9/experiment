import GameMap
import time
import GameTimer
import tkinter as tk
import random


class LifeGame(object):
    def __init__(self, map_rows, map_cols, life_init_ratio):
        # 将在主程序中初始化实例
        self.mapp = GameMap.GameMap(map_rows, map_cols)
        self.mapp.reset(life_init_ratio)
        self.game_timer = GameTimer.GameTimer(self.game_cycle, interval=0.1)  # 创建定时器，每3秒执行一次游戏循环
        # self.game_timer.start()  # 启动定时器
        self.running = False  # 用于跟踪游戏是否在运行
        self.create_buttons()  # 创建开始、暂停和重置按钮
        # timer = GameTimer()

    def create_buttons(self):
        # 创建主应用程序的根窗口
        self.root = tk.Tk()

        # 创建开始按钮
        self.start_button = tk.Button(self.root, text="开始", command=self.start_game)
        self.start_button.pack()

        # 创建暂停按钮
        self.pause_button = tk.Button(self.root, text="暂停", command=self.pause_game)
        self.pause_button.pack()
        self.pause_button.config(state=tk.DISABLED)  # 初始状态下禁用

        # 创建重置按钮
        self.reset_button = tk.Button(self.root, text="重置", command=self.reset_game)
        self.reset_button.pack()
        self.reset_button.config(state=tk.DISABLED)  # 初始状态下禁用

        # 启动主应用程序的事件循环
        self.root.mainloop()

    def game_cycle(self):
        new_grid = [[0] * self.mapp.cols for _ in range(self.mapp.rows)]
        for row in range(1, self.mapp.rows - 1):
            for col in range(1, self.mapp.cols - 1):
                cell_state = self.mapp.get(row, col)
                neighbor_state = self.mapp.get_neighbor_count(row, col)
                if cell_state:
                    if neighbor_state > 3 or neighbor_state < 2:
                        new_grid[row][col] = 0
                    else:
                        new_grid[row][col] = 1
                else:
                    if neighbor_state == 3:
                        new_grid[row][col] = 1
        for row in range(self.mapp.rows):
            for col in range(self.mapp.cols):
                self.mapp.set(row, col, new_grid[row][col])
                # 在这里执行你需要的操作，例如检查细胞状态、更新细胞状态等
        self.mapp.visualize()
        if self.running:
            self.mapp.root.after(100, self.game_cycle)

    def start_game(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.game_cycle()  # 启动游戏循环

    def pause_game(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.running = False
        self.mapp.reset(0.1)  # 使用新的随机配置重置地图
        self.mapp.visualize()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)


st = LifeGame(50, 50, 0.3)
st.mapp.root.mainloop()
