# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(cur):
            if not cur:
                return 0
            return 1 + max(h(cur.left),h(cur.right))

        def helper(cur):
            if not cur:
                return True
            left = h(cur.left)
            right = h(cur.right)
            if abs(left-right) > 1:
                return False
            return helper(cur.left) and helper(cur.right)
        return helper(root)
