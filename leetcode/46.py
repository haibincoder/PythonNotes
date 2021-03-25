"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def find(candidate, use):
            for i in range(len(candidate)):
                temp = candidate[i]
                if len(candidate) > 1:
                    find(candidate[:i] + candidate[i+1:], use + [temp])
                else:
                    result.append(use + [temp])
                    return

        find(nums, [])
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))
