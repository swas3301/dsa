# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        t1 = []
        t2 = []
        cur1 = p
        cur2 = q
        def helper(cur,t):
            if not cur:
                t.append(None)
                return
            t.append(cur.val)
            helper(cur.left,t)
            helper(cur.right,t)
        helper(cur1,t1)
        helper(cur2,t2)
        return t1 == t2
            
        
