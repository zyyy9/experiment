# GameMap.py
import tkinter as tk
import random


class GameMap(object):
    def __init__(self, rows, cols):
        """地图将在逻辑模块进行初始化"""
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=cols * 20, height=rows * 20)
        self.canvas.pack()
        self.visualize()

    def reset(self, life_ratio):
        """重置地图并按life_ratio随机地填充一些活细胞"""
        for row in range(self.rows):
            for col in range(self.cols):
                if row * col == 0 or row == self.rows - 1 or col == self.cols - 1:
                    self.set(row, col, 0)
                else:
                    rnd = random.random()
                    if rnd > 1 - life_ratio:
                        self.grid[row][col] = 1

    def get_neighbor_count(self, row, col):
        """地图上一个方格周围活细胞数是游戏逻辑里的重要数据"""
        res = 0
        for m in range(row - 1, row + 2):
            for n in range(col - 1, col + 2):
                if (m != row or n != col) and self.grid[m][n] == 1:
                    res += 1
        return res

    def set(self, row, col, val):
        """当游戏进行中，需要常常更新地图上方格的状态"""
        self.grid[row][col] = val

    def get(self, row, col):
        """当需要将游戏状态呈现给用户时，就需要获取地图上方格的状态"""
        return self.grid[row][col]

    def visualize(self):
        """生成可视化界面"""
        cell_size = 20
        self.canvas.delete("all")  # Clear the canvas
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                if self.grid[row][col] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

