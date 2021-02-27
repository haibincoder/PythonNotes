"""
题目描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。

输入描述:
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1
输入
10.0.3.193
167969729
输出
167773121
10.3.3.193
"""

def intToIP(input_int):
    input_str = bin(int(input_int)).replace('0b', '')

    padding_length = 32 - len(input_str)
    padding = ''.join(['0' for _ in range(padding_length)])
    input_str = padding + input_str

    index = 0
    result = []
    while index < len(input_str):
        result.append(input_str[index:index+8])
        index += 8

    for i in range(len(result)):
        temp = str(int(result[i], 2))
        result[i] = temp
    result = '.'.join(result)
    return result

def ipToInt(input_ip):
    input_list = input_ip.split('.')

    for i in range(len(input_list)):
        temp = bin(int(input_list[i])).replace('0b', '')
        padding = 8 - len(temp)
        if padding > 0:
            temp = ''.join(['0' for _ in range(padding)]) + temp
        input_list[i] = temp

    result = str(int(''.join(input_list), 2))
    return result


if __name__ == "__main__":
    while True:
        try:
            input_str = input()
            if input_str.isdigit():
                print(intToIP(input_str))
            else:
                print(ipToInt(input_str))

        except Exception as ex:
            break
