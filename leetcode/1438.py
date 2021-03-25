"""
1438. 绝对差不超过限制的最长连续子数组
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

示例 1：

输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。

示例 2：
输入：nums = [10,1,2,4,7,2], limit = 5

输出：4
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
"""
from typing import List

"""
10 1 2 4 7 2
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1
        self.nums = nums
        max_result = 0
        last = nums[0]

        for i in range(len(nums)):
            if len(nums) < max_result + i:
                break
            temp = max(max_result, 1)
            result = None
            for length in range(temp, len(nums)+1):
                if len(nums) < length + i:
                    break
                current_end = nums[i+length - 1]
                if last != current_end or result is None:
                    result = self.getMaxD(i, i+length)
                    last = current_end
                if result <= limit:
                    if length > max_result:
                        max_result = length
                else:
                    break

        return max_result

    def getMaxD(self, start, end):
        max_value = self.nums[start]
        min_value = self.nums[start]
        for item in self.nums[start: end]:
            if item < min_value:
                min_value = item
            if item > max_value:
                max_value = item
        return max_value - min_value


if __name__ == "__main__":
    input_array = [1, 1, 1, 1]
    limit = 4

    solution = Solution()
    print(solution.longestSubarray(input_array, limit))
