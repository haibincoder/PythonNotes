"""
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

   h o r s e
r  0 0 0 0 0
o  0
s  0
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word2 == word1:
            return 0
        elif word1 is None or len(word1) < 1:
            return len(word2)
        elif word2 is None or len(word2) < 1:
            return len(word1)

        matrix = [[0 for _ in range(len(word1)+1)] for j in range(len(word2)+1)]

        for i in range(len(word1)+1):
            matrix[0][i] = i
        for j in range(len(word2)+1):
            matrix[j][0] = j

        for j in range(1, len(word2)+1):
            for i in range(1, len(word1)+1):
                left = matrix[j][i-1] + 1
                top = matrix[j-1][i] + 1
                left_top = matrix[j-1][i-1]
                if word1[i-1] != word2[j-1]:
                    left_top += 1
                matrix[j][i] = min(left, top, left_top)

        return matrix[-1][-1]



if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    solution = Solution()
    print(solution.minDistance(word1, word2))

