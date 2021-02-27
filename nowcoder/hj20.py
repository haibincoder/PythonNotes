"""
题目描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度大于2的子串重复
输入描述:
一组或多组长度超过2的子符串。每组占一行
输出描述:
如果符合要求输出：OK，否则输出NG
示例1
输入
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出
OK
NG
NG
OK
"""

def valid(input_str):
    if len(input_str) <= 8:
        return 'NG'
    result = {}
    for item_char in input_str:
        if item_char.isdigit():
            result['digit'] = 1
        elif item_char.isupper():
            result['upper'] = 1
        elif item_char.islower():
            result['lower'] = 1
        else:
            result['other'] = 1
    if len(result.keys()) < 3:
        return 'NG'

    for i in range(3, len(input_str)):
        sub_str = input_str[i-3:i]
        if input_str.count(sub_str) >= 2:
            return 'NG'
    return 'OK'

import sys
if __name__ == "__main__":

    while True:
        try:
            input_str = input()
            print(valid(input_str))
        except Exception as ex:
            break





