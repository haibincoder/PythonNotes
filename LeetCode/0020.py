"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false
"""


class Solution:
    @staticmethod
    def isValid(s):
        dict = {')':'(', ']':'[', '}':'{'}
        temp_list = []
        for i in range(len(s)):
            length = len(temp_list)
            if length < 1:
                temp_list.append(s[i])
            elif s[i] in dict.keys() and  temp_list[length-1] == dict[s[i]]:
                temp_list.pop(length-1)
            else:
                temp_list.append(s[i])
        result = False
        if len(temp_list) == 0:
            result = True
        return result


if __name__ == "__main__":
    input = '()[]{}'
    result = Solution.isValid(input)
    print(f'{result}')