class Solution:

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        key = '1'
        result = 0
        if n < 1:
            return result
        while n > 0:
            result += str(n).count(key)
            n -= 1
        return result

s = Solution()
print(s.countDigitOne(13))