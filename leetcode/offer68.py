# coding=utf-8
import sys


# str = input()
# print(str)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 超时，字节2021年3月30日
        # 保存节点的所有父节点
        temp = []

        def find(root, use):
            # 搜索回溯所有节点，找到node节点所有父节点
            if root == p:
                use.append(root)
                temp.append(use)
                if len(temp) >= 2:
                    return
            if root == q:
                use.append(root)
                temp.append(use)
                if len(temp) >= 2:
                    return
            if root.left is not None:
                find(root.left, use + [root])
            if root.right is not None:
                find(root.right, use + [root])

        find(root, [])
        temp1 = temp[0]
        temp2 = temp[1]

        # temp1/temp2表示node1,node2所有父节点

        # 求temp1,temp2交集最后一个值
        result = []
        for i in range(len(temp1)):
            for j in range(len(temp2)):
                if temp1[i] == temp2[j]:
                    result.append(temp1[i])
        return result[-1]


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node8
    node3.left = node6
    node3.right = node7

    solution = Solution()

    print(solution.lowestCommonAncestor(node1, node8, node7).val)



