"""
题目描述
牛牛想知道[7,n)内有多少素数，只不过他不知道怎么做，所以他想请你帮忙。
给定一个数字n，返回[7,n)内有多少素数。
示例1
输入
8
返回值
1
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 给定一个数字n，返回[7,n)内有多少素数。
# @param n int整型 代表题目中的n
# @return int整型
#
class Solution:
    def solve(self , n ):
        # 面试直接暴力解就行，这个答案一般记不住
        if n < 8:
            return 0

        is_prime_small = [False for i in range(1000009)]
        is_prime = [False for i in range(1000009)]

        def segment_sieve(a, b):
            i = 0
            while i*i <= b:
                is_prime_small[i] = True
                i += 1
            i = 0
            while i < b-a:
                is_prime[i] = True
                i += 1
            i = 2
            while i*i <= b:
                if is_prime_small[i]:
                    j = 2 * i
                    while j*j <= b:
                        is_prime_small[j] = False
                        j += i
                    j = int(max(2, (a+i-1)/i-1) * i)
                    while j < b:
                        is_prime[j-a] = False
                        j += i
                i += 1

        segment_sieve(7, n)
        ans = 0
        c = n - 7
        for i in range(c):
            if is_prime[i]:
                ans += 1
        return ans

if __name__ == "__main__":
    input_num = 32771
    solution = Solution()
    print(solution.solve(input_num))

