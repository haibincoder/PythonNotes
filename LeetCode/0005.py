'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
'''


def isRepeat(input):
    """
    判断字符串是否回文串
    :param input: aba  abba
    :return:
    """
    return input == input[::-1]

class Solution:
    @staticmethod
    def demo(s):
        length = len(s)
        dp = [[0] * length for _ in length]
        left, right = 0, 0
        for i in range(1, length):
            for j in range(length - i):
                if s[j] == s[j + i] and (j + 1 >= j + i - 1 or dp[j + 1][j + i - 1]):
                    dp[j][j + i] = 1
                    left, right = j, j + i
        return s[left: right + 1]

    @staticmethod
    def longestPalindrome1(s):
        if s == s[::-1]:
            return s
        max_len = 1
        max_str = s[0]
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j-i+1 > max_len and s[i : j+1] == s[i : j+1][::-1]:
                    max_len = j-i+1
                    max_str = s[i, j]
        return max_str

    @staticmethod
    def longestPalindrome(s):
        if s == s[::-1]:
            return s
        max_len = 1
        max_str = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i: j + 1] == s[i: j + 1][::-1]:
                    max_len = j - i + 1
                    max_str = s[i, j]
        return max_str


if __name__ == "__main__":
    input = 'babad'
    # print(f'{isRepeat(input)}')
    result = Solution.longestPalindrome(input)
    print(f'{result}')