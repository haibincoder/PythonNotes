"""
478. 在圆内随机生成点
给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数 randPoint 。

说明:
输入值和输出值都将是浮点数。
圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。
圆周上的点也认为是在圆中。
randPoint 返回一个包含随机点的x坐标和y坐标的大小为2的数组。
示例 1：
输入:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
输出: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

示例 2：
输入:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
输出: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
"""
from typing import List
import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.redius = radius

    def randPoint(self) -> List[float]:
        while True:
            x_random = random.random() * self.redius
            y_random = random.random() * self.redius
            if math.pow(x_random-self.x_center, 2) + math.pow(y_random-self.y_center, 2) <= math.pow(self.redius, 2):
                result = [x_random, y_random]
                # 修改符号
                return result


if __name__ == "__main__":
    obj = Solution(2, 1, 1)
    print(obj.randPoint())


