class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表转list
def ListNodeToList(head):
    list = []
    list.append(head.val)
    while head.next is not None:
        head = head.next
        list.append(head.val)
    return list


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    list1 = ListNodeToList(l1)
    list1.reverse()
    list2 = ListNodeToList(l2)
    list2.reverse()
    result1 = ""
    result2 = ""
    for i in range(0, len(list1)):
        result1 += str(list1[i])
    for i in range(0, len(list2)):
        result2 += str(list2[i])
    result = int(result1) + int(result2)
    result = str(result)
    result2 = []
    for i in range(0,len(result)):
        result2.append(int(result[i]))
    result2.reverse()
    return result2

list = []
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

k1 = ListNode(5)
k2 = ListNode(6)
k1.next = k2

print(addTwoNumbers(l1 = l1, l2 = k1))
