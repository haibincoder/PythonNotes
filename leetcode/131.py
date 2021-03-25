"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例:
    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
"""


def parsestr(s):
    if s is None or len(s) == 0:
        return [[]]
    if len(s) == 1:
        return [[s]]
    result = []
    for i in range(1, len(s)+1):
        left = s[:i]
        right = s[i:]
        if left == left[::-1]:
            right = parsestr(right)
            for i in range(len(right)):
                result.append([left] + right[i])
    return result


if __name__=="__main__":
    input_str = "aabb"
    print(parsestr(input_str))
