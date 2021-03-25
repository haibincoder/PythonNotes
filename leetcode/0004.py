'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。 

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) == 1:
            return nums1[0]

        temp = len(nums1) % 2
        if temp == 0:
            mid_index = int(len(nums1) / 2) - 1
            mid = (nums1[mid_index] + nums1[mid_index+1]) / 2
        else:
            mid_index = int(len(nums1) / 2)
            mid = nums1[mid_index]
        return mid


if __name__ == "__main__":
    num1 = [1, 3]
    num2 = [2]
    solution = Solution()
    result = solution.findMedianSortedArrays(num1, num2)
    print(result)
