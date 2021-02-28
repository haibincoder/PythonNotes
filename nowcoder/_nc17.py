"""
题目描述
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。
给定字符串A以及它的长度n，请返回最长回文子串的长度。

示例1
输入
"abc1234321ab",12
返回值
7

a* b* c* 1 2 3 4 3 2 1 a b

"""

# -*- coding:utf-8 -*-

class Solution:
    def getLongestPalindrome(self, A, n):
        max_len = 0
        for i in range(n):
            odd_sub = A[i-max_len-1: i+1]
            even_sub = A[i-max_len: i+1]
            if i-max_len-1 >= 0 and odd_sub == odd_sub[::-1]:
                max_len += 2
            elif i - max_len >= 0 and even_sub == even_sub[::-1]:
                max_len += 1
        return max_len



    def getLongestPalindrome1(self, A, n):
        # 双指针，【超时】
        if n <= 1:
            return n
        def valid(s):
            return s == s[::-1]
        width = n
        max_result = 2
        while width > max_result:
            for i in range(len(A)):
                if i + max_result > len(A):
                    break
                for j in range(i+1, len(A)):
                    if valid(A[i:j]):
                        max_result = max(max_result, j-i)
            width -= 1
        return max_result

if __name__ == "__main__":
    input_str = 'baabccc'
    solution = Solution()
    print(solution.getLongestPalindrome(input_str, len(input_str)))