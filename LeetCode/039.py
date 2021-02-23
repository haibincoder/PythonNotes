"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        def find(idx, use, remind):
            for i in range(idx, len(candidates)):
                temp = remind - candidates[i]
                if temp == 0:
                    sub_result = use + [candidates[i]]
                    sub_result.sort()
                    if sub_result not in result:
                        result.append(sub_result)
                elif temp > 0:
                    find(idx, use + [candidates[i]], remind - candidates[i])
                elif temp < 0:
                    return

        find(0, [], target)

        return result

if __name__ == "__main__":
    input_arr = [2,6,3,7]
    target = 7

    solution = Solution()
    print(solution.combinationSum(input_arr, target))