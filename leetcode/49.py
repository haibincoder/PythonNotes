"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dic = {}
        for item in strs:
            temp = ''.join(sorted(item))
            if temp in temp_dic:
                temp_dic[temp].append(item)
            else:
                temp_dic[temp] = [item]
        result = []
        for item in temp_dic:
            result.append(temp_dic[item])

        return result


if __name__ == "__main__":
    input_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(input_arr))
