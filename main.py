

class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


import collections
def printTree(node):
    result = []

    que = collections.deque()
    que.append(node)
    while len(que) > 0:
        temp_node = que.popleft()
        result.append(temp_node.val)
        if temp_node.left is not None:
            que.append(temp_node.left)
        if temp_node.right is not None:
            que.append(temp_node.right)
    return result


if __name__ == "__main__":
    root = Node(1, None, None)
    node1 = Node(2, None, None)
    node2 = Node(3, None, None)
    node3 = Node(4, None, None)
    root.left = node1
    root.right = node2
    node2 = node3
    print(printTree(root))





