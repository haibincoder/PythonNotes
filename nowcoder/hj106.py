"""
题目描述
将一个字符串str的内容颠倒过来，并输出。str的长度不超过100个字符。


输入描述:
输入一个字符串，可以有空格

输出描述:
输出逆序的字符串
"""


if __name__ == "__main__":
    input_str = list(input())

    input_str = ''.join(input_str[::-1])

    print(input_str)


