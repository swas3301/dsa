# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None

        cur = head
        n = 1
        while cur.next:
            n = n + 1 
            cur = cur.next
        
        cur.next = head
        k = k % n
        for i in range(n - k):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
        
