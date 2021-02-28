"""
题目描述
现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。


注：

称重重量包括0


输入描述:
输入包含多组测试数据。

对于每组测试数据：

第一行：n --- 砝码数(范围[1,10])

第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])

第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
输出描述:
利用给定的砝码可以称出的不同的重量数
示例1
输入
复制
2
1 2
2 1
输出
复制
5
"""


if __name__ == "__main__":
    while True:
        try:
            lenght = input()
            weight_list = input().split()
            weight_list = [int(i) for i in weight_list]
            num_list = input().split()
            num_list = [int(i) for i in num_list]

            input_list = []
            for index in range(len(weight_list)):
                temp = [weight_list[index] for i in range(num_list[index])]
                input_list.extend(temp)
            result_set = set()
            result_set.add(0)

            for index in range(len(input_list)):
                temp_set = set()
                for item in result_set:
                    temp = item + input_list[index]
                    temp_set.add(temp)
                for item in temp_set:
                    result_set.add(item)
                result_set.add(input_list[index])
            print(len(result_set))

        except Exception as ex:
            break
