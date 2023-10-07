import GameMap
import time
import GameTimer

class LifeGame(object):
    def __init__(self, map_rows, map_cols, life_init_ratio):
        # 将在主程序中初始化实例
        self.mapp = GameMap.GameMap(map_rows, map_cols)
        self.mapp.reset(life_init_ratio)
        self.game_timer = GameTimer.GameTimer(self.game_cycle, interval=0.1)  # 创建定时器，每3秒执行一次游戏循环
        self.game_timer.start()  # 启动定时器
        # timer = GameTimer()


    def game_cycle(self):
        # 进行一次游戏循环，将在此完成地图的更新，将在计时器触发时被调用
        for row in range(1, self.mapp.rows-1):
            for col in range(1, self.mapp.cols-1):
                cell_state = self.mapp.get(row, col)
                neighbor_state = self.mapp.get_neighbor_count(row, col)
                if cell_state == True:
                    if neighbor_state > 3 or neighbor_state < 2:
                        self.mapp.set(row, col, 0)
                else:
                    if neighbor_state == 3:
                        self.mapp.set(row, col, 1)
                # 在这里执行你需要的操作，例如检查细胞状态、更新细胞状态等
        self.mapp.visualize()

st = LifeGame(50, 50, 0.3)
st.mapp.root.mainloop()
