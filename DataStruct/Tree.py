# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        stack = [root]
        while len(stack) > 0:
            p = stack.pop()
            result.append(p.val)
            if p.right is not None:
                stack.append(p.right)
            if p.left is not None:
                stack.append(p.left)
        return result

    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def minDepth(self, root):
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left,right) + 1

    def levelOrder(self, root):
        result = []
        queue = [root]
        while len(queue) > 0:
            item = queue[0]
            queue.remove(item)
            result.append([item.val])
            if item.left is not None:
                queue.append(item.left)
            if item.right is not None:
                queue.append(item.right)
        return result


s = Solution()

tree0 = TreeNode(3)
tree1 = TreeNode(9)
tree2 = TreeNode(20)
tree3 = TreeNode(15)
tree4 = TreeNode(7)
tree0.left = tree1
tree0.right = tree3
tree2.left = tree4
tree2.right = tree4

print(s.minDepth(tree0))