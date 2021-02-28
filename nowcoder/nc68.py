"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
示例1
输入
1
返回值
1
示例2
输入
4
返回值
5
"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        result = [1, 1, 2]
        i = 3
        while len(result) <= number:
            result.append(result[i-1] + result[i-2])
            i += 1

        return result[-1]



if __name__ == "__main__":
    target = 4
    solution = Solution()
    print(solution.jumpFloor(target))

