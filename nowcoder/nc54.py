"""
题目描述
给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。
注意：
三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
解集中不能包含重复的三元组。
例如，给定的数组 S = {-10 0 10 20 -10 -40},解集为(-10, 0, 10) (-10, -10, 20)
示例1
输入
[-2,0,1,1,2]
返回值
[[-2,0,2],[-2,1,1]]
"""

#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def threeSum(self, num):
        result = []
        if len(num) < 3:
            return []
        num.sort()
        for i in range(len(num) - 2):
            if num[i] > 0:
                break
            target = 0 - num[i]

            left = i + 1
            right = len(num) - 1
            while left < right:
                if target - num[left] < 0:
                    break
                if num[left] + num[right] == target:
                    result.append([num[i], num[left], num[right]])
                    left += 1
                elif num[left] + num[right] > target:
                    right -= 1
                else:
                    left += 1

        return result


    def threeSum2(self, num):
        # 排序+双指针
        result = []

        num.sort()
        length = len(num)

        for i in range(length-2):
            is_end_i = False
            for j in range(i+1, length-1):
                temp = num[i] + num[j]
                if temp > 0:
                    is_end_i = True
                    break
                is_end = False
                for end in range(j+1, length):
                    if temp + num[end] == 0:
                        result.append([num[i], num[j], num[end]])
                    elif temp + num[end] > 0:
                        is_end = True
                        break
                if is_end:
                    break
            if is_end_i:
                break
        return result

if __name__ == "__main__":
    input_arr = [-2,0,1,1,2]
    solution = Solution()
    print(solution.threeSum(input_arr))