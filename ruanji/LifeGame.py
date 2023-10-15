import GameMap
import GameTimer
import tkinter as tk


class LifeGame(object):
    def __init__(self, map_rows, map_cols, life_init_ratio):
        # 将在主程序中初始化实例
        self.mapp = GameMap.GameMap(map_rows, map_cols)
        self.mapp.reset(life_init_ratio)
        self.game_timer = GameTimer.GameTimer(self.game_cycle, interval=0.1)  # 创建定时器，每3秒执行一次游戏循环
        self.create_buttons()  # 创建开始、暂停和重置按钮
        self.grid_set = set()


    def create_buttons(self):
        # 创建主应用程序的根窗口
        self.root = self.mapp.root
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side="bottom", fill="x")
        # 创建重置按钮
        self.reset_button = tk.Button(self.button_frame, text="重置", command=self.reset_game)
        self.reset_button.pack(side="right", padx=10, pady=10)

        # 创建暂停按钮
        self.pause_button = tk.Button(self.button_frame, text="暂停", command=self.pause_game)
        self.pause_button.pack(side="right", padx=10, pady=10)

        # 创建开始按钮
        self.start_button = tk.Button(self.button_frame, text="开始", command=self.start_game)
        self.start_button.pack(side="right", padx=10, pady=10)


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

        if self.game_timer.running:
            # 检测游戏是否进入稳定状态
            if not self.check_stability():
            # 将当前格子状态转换为可哈希的元组
                current_state = tuple(tuple(row) for row in self.mapp.grid)
            # 将当前格子状态添加到集合中
                self.grid_set.add(current_state)


    def start_game(self):
        self.game_timer.running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.grid_set.clear()
        self.game_timer.start()  # 启动游戏循环

    def pause_game(self):
        self.game_timer.running = False
        self.game_timer.stop()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.game_timer.running = False
        self.mapp.reset(0.3)  # 使用新的随机配置重置地图
        self.mapp.visualize()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def check_stability(self):
        # 将现在细胞状态转化为元组，利于比较
        current_state = tuple(tuple(row) for row in self.mapp.grid)
        for state in self.grid_set:
            if state == current_state:
                # 如果进入稳定状态，调用弹窗函数
                self.game_timer.running = False
                self.show_stability_popup()
                self.game_timer.stop()
                return True
        return False

    def show_stability_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("稳定状态提示")
        label = tk.Label(popup, text="游戏已进入稳定状态！", padx=20, pady=20)
        label.pack()
        close_button = tk.Button(popup, text="关闭", command=popup.destroy)
        close_button.pack()
