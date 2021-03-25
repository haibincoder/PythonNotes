"""
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：
输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
"""


class Solution:
    def transpose(self, matrix):
        width = len(matrix[0])
        height = len(matrix)

        result = [[0 for j in range(height)] for i in range(width)]

        for i in range(width):
            for j in range(height):
                result[i][j] = matrix[j][i]
        return result


if __name__ == "__main__":
    input_array = [[1, 2, 3], [4, 5, 6]]

    solution = Solution()

    result = solution.transpose(input_array)
    print(result)


