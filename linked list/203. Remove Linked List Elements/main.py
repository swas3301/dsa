# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        test = ListNode(next = head)
        prev, curr = test, head
        while curr:
            new = curr.next
            if curr.val == val:
                prev.next = new
            else:
                prev = curr
            curr = new
        return test.next
