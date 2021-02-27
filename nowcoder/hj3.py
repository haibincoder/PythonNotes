"""
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。


注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。

当没有新的输入时，说明输入结束。

输入描述:
注意：输入可能有多组数据。每组数据都包括多行，第一行先输入随机整数的个数N，接下来的N行再输入相应个数的整数。具体格式请看下面的"示例"。

输出描述:
返回多行，处理后的结果

示例1
输入
复制
3
2
2
1
11
10
20
40
32
67
40
20
89
300
400
15
输出
复制
1
2
10
15
20
32
40
67
89
300
400
"""


import sys

def getInput():
    input_arr = []
    temp = None
    length = None
    for item in sys.stdin:
        if length is None:
            length = int(item)
            temp = []
        else:
            temp.append(int(item))
            length -= 1

            if length == 0:
                input_arr.append(temp)
                length = None
    return input_arr


if __name__ == "__main__":
    input_arr = getInput()

    for index in range(len(input_arr)):
        temp = input_arr[index]
        temp = list(set(temp))
        temp.sort()
        input_arr[index] = temp

    for item in input_arr:
        for sub_item in item:
            print(sub_item)
