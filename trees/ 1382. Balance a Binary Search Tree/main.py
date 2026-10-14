# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        def inorder(node, vals):
            if not node:
                return None
            inorder(node.left,vals)
            vals.append(node.val)
            inorder(node.right,vals)

        def build(vals, left, right):
            if left > right:
                return None
            mid = (left + right)//2
            node = TreeNode(vals[mid])
            node.left = build(vals, left, mid -1)
            node.right = build(vals, mid + 1, right)
            return node

        vals = []
        inorder(root,vals)
        
        
        return build(vals, 0, len(vals)-1)
