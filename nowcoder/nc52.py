"""
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
"""


#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s):
        # wrte code here
        if len(s) % 2 != 0:
            return False

        temp = []
        char_dict = {'[': ']', '{': '}', '(': ')'}

        for item in s:
            if item in char_dict.keys():
                temp.append(item)
            else:
                if len(temp) < 1:
                    return False
                temp_char = temp.pop()
                if item != char_dict[temp_char]:
                    return False
        if len(temp) > 0:
            return False
        return True


if __name__ == "__main__":
    input_arr = '[()]'
    solution = Solution()
    print(solution.isValid(input_arr))
