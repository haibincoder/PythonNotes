"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            if l2 is None:
                return ListNode()
            else:
                return l2
        if l2 is None:
            return l1

        result = None
        result_point = None

        l1_point = l1
        l2_point = l2

        while True:
            temp = None
            if l1_point is None:
                temp = l2_point
                l2_point = l2_point.next
            elif l2_point is None:
                temp = l1_point
                l1_point = l1_point.next
            elif l1_point.val <= l2_point.val:
                temp = l1_point
                l1_point = l1_point.next
            else:
                temp = l2_point
                l2_point = l2_point.next

            if result is None:
                result = ListNode(temp.val)
                result_point = result
            else:
                result_point.next = ListNode(temp.val)
                result_point = result_point.next
            if l1_point is None and l2_point is None:
                break

        return result

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    solution = Solution()
    print(solution.mergeTwoLists(l1, l2))