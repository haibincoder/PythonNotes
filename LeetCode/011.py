"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2
"""
from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        # 超时
        if height is None or len(height) <= 1:
            return 0

        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                temp = min(height[i], height[j])
                area = temp * (j - i)
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        if height is None or len(height) <= 1:
            return 0

        i = 0
        j = len(height) - 1
        max_area = 0

        while i <= j:
            temp = min(height[i], height[j]) * (j-i)
            if temp > max_area:
                max_area = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__=="__main__":
    arr = [1,8,6,2,5,4,8,3,7]

    solution = Solution()
    print(solution.maxArea(arr))
