"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：
输入：matrix = [[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]

"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix is None:
            return []

        width = len(matrix[0])
        heigh = len(matrix)

        result = [[0 for i in range(heigh)] for j in range(width)]

        for col in range(heigh):
            for row in range(width):
                result[row][col] = matrix[col][row]
        return result


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    solution = Solution()
    print(solution.transpose(matrix=matrix))