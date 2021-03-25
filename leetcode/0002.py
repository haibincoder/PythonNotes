'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        current = l1
        input_1 = ''
        while current:
            input_1 += str(current.val)
            current = current.next
        num_1 = list(input_1)[::-1]

        input_2 = ''
        current = l2
        while current:
            input_2 += str(current.val)
            current = current.next
        num_2 = list(input_2)
        num_2.reverse()

        result_num = str(int(''.join(num_1)) + int(''.join(num_2)))
        result_num = list(result_num)
        result_num.reverse()
        result = ListNode(result_num[0])
        current_node = result
        for i in range(1, len(result_num)):
            new_node = ListNode(int(result_num[i]))
            current_node.next = new_node
            current_node = current_node.next
        return result


if __name__ == "__main__":
    node_2 = ListNode(2)
    node_4 = ListNode(4)
    node_3 = ListNode(3)
    node_2.next = node_4
    node_4.next = node_3

    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_4 = ListNode(4)
    node_5.next = node_6
    node_6.next = node_4

    
    solution = Solution()
    result = solution.addTwoNumbers(node_2, node_5)
    print(f'{result}')

