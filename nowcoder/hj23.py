"""
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1
输入
abcdd
aabcddd
输出
dd
aaddd
"""

def countChar(input_str):
    result = {}
    for item_char in input_str:
        if item_char in result.keys():
            result[item_char] = result[item_char] + 1
        else:
            result[item_char] = 1
    return result


if __name__ == "__main__":
    while True:
        try:
            input_str = input()
            count_result = countChar(input_str)

            min_count = None
            min_keys = []
            for char_key in count_result.keys():
                count = count_result[char_key]
                if min_count is None:
                    min_count = count
                if count < min_count:
                    min_count = count
                    min_keys = [char_key]
                elif count == min_count:
                    min_keys.append(char_key)
            for item in min_keys:
                input_str = input_str.replace(item, '')
            print(input_str)
        except Exception as ex:
            break