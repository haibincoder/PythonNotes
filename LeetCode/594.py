import collections


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        d = collections.Counter(nums)
        for item in nums:
            if item + 1 in d:
                ans = max(ans, d[item] + d[item + 1] )
        return ans

s = Solution()
input = [1,3,2,2,5,2,3,7]
print(s.findLHS(input))
