"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
"""

from typing import List
import math


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums[index] = int(math.pow(nums[index], 2))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums


if __name__ == "__main__":
    input_arr = [-4, -1, 0, 3, 10]

    solution = Solution()
    print(solution.sortedSquares(input_arr))