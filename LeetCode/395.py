"""
395. 至少有 K 个重复字符的最长子串
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

示例 1：
输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2：
输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 超时
        if len(s) < k:
            return 0
        width = len(s)

        while width >= k:
            for i in range(len(s)):
                if i + width >= len(s):
                    if self.valid(s[i:i+width], k):
                        return width
                sub_str = s[i:i+width]
                if sub_str[-1] == s[i-1]:
                    continue
                if self.valid(sub_str, k):
                    return width
            width -= 1
        return 0

    def valid(self, sub_str, k):
        char_set = set(sub_str)

        for item_char in char_set:
            if sub_str.count(item_char) < k:
                return False
        return True


if __name__ == "__main__":
    input_str = 'a'
    k = 1
    solution = Solution()
    print(solution.longestSubstring(input_str, k))