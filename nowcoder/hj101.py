"""
题目描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）

本题有多组输入，请使用while(cin>>)处理

输入描述:
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述:
输出排好序的数字

示例1
输入
复制
8
1 2 4 9 3 55 64 25
0
5
1 2 3 4 5
1
输出
复制
1 2 3 4 9 25 55 64
5 4 3 2 1
"""

if __name__ == "__main__":
    while True:
        try:
            length = input()
            input_list = input().strip().split(' ')
            input_list = [int(item) for item in input_list]
            isreverse = int(input())

            if isreverse:
                input_list.sort(reverse=True)
            else:
                input_list.sort()
            input_list = [str(item) for item in input_list]
            input_list = ' '.join(input_list)

            print(input_list)
        except Exception as ex:
            break

