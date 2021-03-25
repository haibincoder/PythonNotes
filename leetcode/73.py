"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？

示例 1：
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
示例 2：
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setColZeros(matrix, row, col_length):
            for i in range(col_length):
                matrix[i][row] = 0
        def setRowZeros(matrix, col, row_length):
            for i in range(row_length):
                matrix[col][i] = 0

        m = len(matrix)
        n = len(matrix[0])

        temp = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    temp.append([i, j])

        for item in temp:
            setColZeros(matrix, item[1], m)
            setRowZeros(matrix, item[0], n)


if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)
