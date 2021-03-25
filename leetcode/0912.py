"""
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""

class Solution:
    @staticmethod
    def sortArray1(nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums

    @staticmethod
    def sortArray(nums):
        nums.sort()
        return nums


if __name__ == "__main__":
    input = [5,2,3,1]
    result = Solution.sortArray(input)
    print(f'{result}')