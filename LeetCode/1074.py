"""
给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。
如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。

示例 1：
输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
输出：4
解释：四个只含 0 的 1x1 子矩阵。
示例 2：
输入：matrix = [[1,-1],[-1,1]], target = 0
输出：5
解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
"""
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        self.matrix = matrix
        rows = len(matrix[0])
        cols = len(matrix)

        final_result = 0
        for x in range(rows):
            for y in range(cols):
                for hei in range(cols-y):
                    for wid in range(rows - x):
                        x2 = x+wid
                        y2 = y+hei
                        temp = self.getCount(x, y, x2, y2)
                        if target == temp:
                            final_result += 1
        return final_result

    def getCount(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return self.matrix[y1][x1]
        result = 0
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                result += self.matrix[y][x]
        return result


if __name__ == "__main__":
    input_matrix = [[0,1,1,0,1,0,0],[0,0,1,0,0,1,0],[1,0,0,0,1,1,0],[1,1,0,1,1,1,0],[0,1,1,1,1,1,1]]
    target = 0
    solution = Solution()
    print(solution.numSubmatrixSumTarget(input_matrix, target))