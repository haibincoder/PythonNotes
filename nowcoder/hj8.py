"""
题目描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
复制
4
0 1
0 2
1 2
3 4
输出
复制
0 3
1 2
3 4
"""

if __name__ == "__main__":
    length = int(input())
    result = {}
    for i in range(length):
        index, value = input().strip().split(' ')

        index, value = int(index), int(value)

        if index in result.keys():
            result[index] = result[index] + int(value)
        else:
            result[index] = int(value)

    for key in sorted(result.keys()):
        print(f'{key} {result[key]}')
