import math


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n / 5 < 5:
            return int(n / 5)
        else:
            return  int(n / 5) + self.trailingZeroes( int(n / 5))

s = Solution()
print(s.trailingZeroes(7))