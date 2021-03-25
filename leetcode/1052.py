"""
1052. 爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        result = 0
        if len(customers) == 0:
            return 0
        if len(customers) < X:
            for item in customers:
                result += item
            return result

        temp_arr = []
        for i in range(len(customers)):
            if grumpy[i] == 0:
                temp_arr.append(0)
            else:
                temp_arr.append(customers[i])
        # temp_arr = [0, 0, 0, 2, 0, 1, 0, 5]
        #            [0, 1, 0, 1, 0, 1, 0, 1]

        max_total = 0
        max_index = 0
        for i in range(len(temp_arr)):
            if i + X > len(temp_arr):
                break
            temp = self.getWindowCount(temp_arr, i, i + X)
            if temp > max_total:
                max_total = temp
                max_index = i

        for i in range(max_index, max_index+X):
            grumpy[i] = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                result += customers[i]

        return result

    def getWindowCount(self, nums, start, end):
        temp = nums[start: end]
        temp_result = 0
        for item in temp:
            temp_result += item
        return temp_result


if __name__ == "__main__":
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3

    solution = Solution()
    print(solution.maxSatisfied(customers, grumpy, X))
