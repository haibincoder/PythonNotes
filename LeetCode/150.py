"""
150. 逆波兰表达式求值
根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。



说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：

输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []

        for item in tokens:
            if item == '+':
                temp = arr.pop() + arr.pop()
                arr.append(temp)
            elif item == '-':
                temp1 = arr.pop()
                temp2 = arr.pop()
                temp = int(temp2 - temp1)
                arr.append(temp)
            elif item == '*':
                temp = arr.pop() * arr.pop()
                arr.append(temp)
            elif item == '/':
                temp1 = arr.pop()
                temp2 = arr.pop()
                temp = int(temp2 / temp1)
                arr.append(temp)
            else:
                arr.append(int(item))
        return arr[0]


if __name__ == "__main__":
    tokens = ["4","13","5","/","+"]
    solution = Solution()
    print(solution.evalRPN(tokens))