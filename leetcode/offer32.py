"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        import collections
        que = collections.deque()
        que.append([root, 0])

        result = []

        while len(que) > 0:
            node = que.popleft()
            node, level = node[0], node[1]
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)
            level += 1
            if node.left is not None:
                que.append([node.left, level])
            if node.right is not None:
                que.append([node.right, level])

        for index in range(len(result)):
            if index % 2 == 1:
                result[index].reverse()
        return result


if __name__ == "__main__":
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    root.left = node1
    root.right = node2

    solution = Solution()
    print(solution.levelOrder(root))
