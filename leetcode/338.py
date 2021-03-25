"""
338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0 for _ in range(num + 1)]
        for item in range(num+1):
            temp = bin(item).replace('0b', '').count('1')
            result[item] = temp
        return result


if __name__ == "__main__":
    input_str = 2
    solution = Solution()
    print(solution.countBits(input_str))