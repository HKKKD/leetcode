# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = head
        temp = head.next
        while temp:
            if temp.val == pre.val:
                pre.next = temp.next
                temp = temp.next
            else:
                pre = temp
                temp = temp.next
        return head
            