"""
896. 单调数列
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。


示例 1：
输入：[1,2,2,3]
输出：true
示例 2：
输入：[6,5,4,4]
输出：true
示例 3：
输入：[1,3,2]
输出：false
示例 4：
输入：[1,2,4,5]
输出：true
示例 5：
输入：[1,1,1]
输出：true
"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A is None or len(A) == 0:
            return False
        if len(A) == 2:
            return True

        is_reverse = None
        for index in range(1, len(A)):
            if A[index] == A[index-1]:
                continue
            elif A[index] > A[index-1]:
                if is_reverse is None:
                    is_reverse = False
                elif is_reverse:
                    return False
            elif A[index] < A[index-1]:
                if is_reverse is None:
                    is_reverse = True
                elif not is_reverse:
                    return False
        return True

        # sort = sorted(A)
        # reve = sorted(A, reverse=True)
        #
        # if A == sort or A == reve:
        #     return True
        # return False

if __name__ == "__main__":
    input_arr = [6,5,4,2]

    solution = Solution()
    print(solution.isMonotonic(input_arr))
