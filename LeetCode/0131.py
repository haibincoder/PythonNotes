"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s is None or len(s) < 1:
            return [[]]
        if len(s) == 1:
            return [[s]]

        result = []

        for index in range(1, len(s)):
            left = s[:index]
            right = s[index:]

            if left == left[::-1]:
                right_list = self.partition(right)
                for item in right_list:
                    result.append([left] + item)

        return result


if __name__ == "__main__":
    input_str = "aab"
    solution = Solution()
    print(solution.partition(input_str))
