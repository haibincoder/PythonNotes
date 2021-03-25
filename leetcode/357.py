"""
357. 计算各个位数不同的数字个数
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:
输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        n = min(n, 10)
        ans = 10
        base = 9
        _sum = 9
        for i in range(1, n):
            _sum = _sum * base
            ans = ans + _sum
            base -= 1
        return ans


    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return 10
    #
    #     self.result = 0
    #     self.find('', 0, n)
    #     return self.result
    #
    # def find(self, use, depth, n):
    #     if depth == n:
    #         temp = str(int(use))
    #         temp_set = set(temp)
    #         if len(temp) == len(temp_set):
    #             self.result += 1
    #         return
    #     else:
    #         depth += 1
    #         for item_char in range(0, 10):
    #             if item_char != 0 and str(item_char) in use:
    #                 continue
    #             self.find(use + str(item_char), depth, n)


if __name__ == "__main__":
    n = 3
    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(n))