class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        pre = temp
        while temp.next:
            cur = temp.next
            if cur.val == val:
                temp.next = cur.next
                continue
            temp = temp.next
        return pre.next