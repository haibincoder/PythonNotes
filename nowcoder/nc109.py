"""
题目描述
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。
示例1
输入
[[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]
返回值
3

[[1,1,0,0,0],
 [0,1,0,1,1],
 [0,0,0,1,1],
 [0,0,0,0,0],
 [0,0,1,1,1]]

"""

#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
class Solution:
    def solve(self, grid):
        ans = 0

        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == '1' or grid[j][i] == 1:
                    ans += 1
                    self.check(grid, i, j)
        return ans

    def check(self, grid, i, j):
        col = len(grid)
        row = len(grid[0])

        if i < 0 or j < 0 or i >= row or j >= col or grid[j][i] == 0 or grid[j][i] == '0':
            return
        grid[j][i] = 0
        self.check(grid, i - 1, j)
        self.check(grid, i + 1, j)
        self.check(grid, i, j - 1)
        self.check(grid, i, j + 1)


if __name__ == "__main__":
    input_arr = [[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]
    solution = Solution()
    print(solution.solve(input_arr))