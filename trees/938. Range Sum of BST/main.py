# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0

        def helper(cur):
            nonlocal s
            if not cur: return 
            if cur.val>=low and cur.val<=high:
                s = s + cur.val
            helper(cur.left)
            helper(cur.right)
        helper(root)
        return s
