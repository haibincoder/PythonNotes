"""
给定一个二叉树，返回它的 前序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal1(self, root):
        result = []
        def helper(root):
            if root is None or root.val is None:
                return
            result.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return result

    def preorderTraversal(self, root):
        if root is None or root.val is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = solution.preorderTraversal(root)
    print(f'{result}')