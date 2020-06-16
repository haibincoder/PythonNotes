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
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        temp = len(nums1) % 2
        if temp == 1:
            middle = nums1[int((len(nums1)+1)/2 - 1)]
        else:
            middle = nums1[int((len(nums1)) / 2)] + nums1[int((len(nums1)) / 2) - 1]
            middle = middle/2
        return middle


if __name__ == "__main__":
    num1 = [1, 3]
    num2 = [2, 4]
    result = Solution.findMedianSortedArrays(num1, num2)
    print(f'{result}')
