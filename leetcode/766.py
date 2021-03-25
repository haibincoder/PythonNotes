"""
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

输入：matrix = [[1,2],[2,2]]
输出：false
解释：
对角线 "[1, 2]" 上的元素不同。
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        if len(matrix[0]) == 1:
            return True

        col = len(matrix)
        row = len(matrix[0])
        temp = None
        for index in range(col):
            if temp is None:
                temp = matrix[index][0: row-1]
            else:
                current = matrix[index][1: row]
                if current != temp:
                    return False
                else:
                    temp = matrix[index][0: row-1]
        return True


if __name__ == "__main__":
    input_arr = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    solution = Solution()
    print(solution.isToeplitzMatrix(input_arr))