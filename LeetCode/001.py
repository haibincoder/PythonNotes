class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key_index = {}
        for index, item in enumerate(nums):
            temp = target-item
            if temp in key_index:
                return [key_index[temp], index]
            else:
                key_index[item] = index


if __name__ == "__main__":
    soulution = Solution()
    input = [2, 7, 11, 15]
    target = 9
    print(soulution.twoSum(input, target))
