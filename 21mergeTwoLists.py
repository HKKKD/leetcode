# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        temp = pre
        while temp.next and temp.next.next:
            p1 = temp.next
            p2 = temp.next.next
            temp.next, p1.next, p2.next = p2, p2.next, p1
            temp = temp.next.next
        return pre.next