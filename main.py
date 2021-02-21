"""
Q-A匹配：
编辑距离

    a  b  c  d  a
a   1  0  0  0  1
b   0  1  0  0  0
e   0  0  0  0  0
f   0  0  0  0  0


   a b c d e    1
a  1 0 0 0 0
c  0 0 1 0 0
d  0 0 0 1 0
e  0 0 0 0 1
"""

def editDistance(input_a, input_b):
    # plan2 构建矩阵，计算不同的部分
    # 构建 n * m 矩阵
    matrix = [0] * len(input_a)
    for i in range(len(input_a)):
        matrix[i] = [0] * len(input_b)

    # 分别计算 input_a、input_b各个字符是否相似
    for i in range(input_a):
        for j in range(input_b):
            if input_a[i] == input_b[j]:
                matrix[i][j] = 1

    # 计算有多少列全是0
    diff = 0
    for i in range(len(input_a)):
        tmp = 0
        for j in range(len(input_b)):
            tmp += matrix[i][j]
        if tmp == 0:
            diff += 1
    return diff

    # plan1 计算相同的部分
    # 考虑插入情况
    # same = 0
    # maxlength = len(input_a) if len(input_a) > len(input_b) else len(input_b)
    #
    # for i in range(maxlength):
    #     if i > len(input_a) - 1:
    #         break
    #     if i > len(input_b) - 1:
    #         break
    #     if input_a[i] == input_b[i]:
    #         same += 1
    # return maxlength - same

    # plan3
    # dp算法


if __name__ == "__main__":
    input_a = "abcde"
    input_b = "abef"
    input_c = "acde"

    print(editDistance(input_a, input_b))
    print(editDistance(input_a, input_c))