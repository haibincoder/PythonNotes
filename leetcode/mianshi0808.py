"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:
 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:
 输入：S = "ab"
 输出：["ab", "ba"]
"""
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:

        self.result = []

        self.find('', S)
        self.result.sort()
        return self.result

    def find(self, use, remind):
        if len(remind) <= 1:
            use += remind
            if use not in self.result:
                self.result.append(use)
            return
        for index in range(len(remind)):
            temp = remind[index]
            self.find(use + temp , remind[0:index] + remind[index+1:])


if __name__ == "__main__":
    input_str = 'qqe'
    solution = Solution()
    print(solution.permutation(input_str))