"""
题目描述
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。

输入描述:
输入一个算术表达式

输出描述:
得到计算结果

示例1
输入
3+2*{1+2*[-4/(8-6)+7]}
输出
25
"""

if __name__ == "__main__":
    input_str = input()

    input_str = input_str.replace('[', '(')
    input_str = input_str.replace(']', ')')
    input_str = input_str.replace('{', '(')
    input_str = input_str.replace('}', ')')

    print(eval(input_str))

