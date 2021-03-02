"""
304. 二维区域和检索 - 矩阵不可变
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

Range Sum Query 2D
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例：
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # 前缀和
        # self.pre_sum = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if j == 0:
        #             self.pre_sum[i][j] = matrix[i][j]
        #         else:
        #             self.pre_sum[i][j] = self.pre_sum[i][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                result += self.matrix[i][j]

        # 前缀和
        # for row in range(row1, row2+1):
        #     result += (self.pre_sum[row][col2] - self.pre_sum[row][col1] + + self.matrix[row][col1])

        return result

# 方案1： 暴力查
# 方案2： 每一行计算前缀和

if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4],
        [5, 6, 3, 2],
        [1, 2, 0, 1],
        [4, 1, 0, 1],
        [1, 0, 3, 0]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))
