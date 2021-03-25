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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None
        length = len(s)
        if length < 2:
            return s

        matrix = [[False] * length for _ in range(length)]

        for i in range(length):
            matrix[i][i] = True

        begin = 0
        maxlength = 0
        for j in range(length):
            for i in range(j):
                if s[i] != s[j]:
                    matrix[i][j] = False
                else:
                    if j-i < 2:
                        matrix[i][j] = True
                    else:
                        matrix[i][j] = matrix[i+1][j-1]
                    if j-i > maxlength and matrix[i][j] is True:
                        begin = i
                        maxlength = j-i
        return s[begin: begin + maxlength + 1]


if __name__ == "__main__":
    solution = Solution()
    input = 'aaaa'
    # print(f'{isRepeat(input)}')
    print(solution.longestPalindrome(input))