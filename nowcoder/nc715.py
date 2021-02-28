"""
题目描述
牛牛特别喜欢数字7，他想知道如果一个数字n乘以7是否是一个素数。
给定一个数字n，如果该数乘以7是一个素数，返回"YES"，否则，返回"NO"。
示例1
输入
复制
1
返回值
"YES"
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 给定一个数字n，如果该数乘以7是一个素数，返回"YES"，否则，返回"NO"。
# @param n int整型 代表题目中的n
# @return string字符串
#
class Solution:
    def solve(self , n ):
        # write code here
        # 判断是否为素数
        def isPrime(num):
            if num < 2:
                return 'NO'
            for i in range(2, num):
                if num % i == 0:
                    return 'NO'
            return 'YES'
        return isPrime(n * 7)


if __name__ == "__main__":
    input_arr = 1
    solution = Solution()
    print(solution.solve(input_arr))