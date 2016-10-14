# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        if head.val == head.next.val:
            return True
        fast = head
        slow = head
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        sechead = slow.next
        slow.next = None
        p1 = sechead
        p2 = p1.next
        while p1 and p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        sechead.next = None
        q1 = p2
        q2 = head
        while q1:
            if q1 != q2:
                return False
            q1 = q1.next
            q2 = q2.next
        return True