'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution:
    def twoSum(self, nums, target):
        key_value = {}
        for index, value in enumerate(nums):
            another = target - value
            if another in key_value:
                return [index, key_value[another]]
            key_value[value] = index


if __name__ == "__main__":
    input = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(input, target)
    print(f'{result}')