# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        cur = root
        if not cur:
            return True
        else:
            left,right = cur.left,cur.right
            res1 = []
            res2 = []
            def helper1(root,res):
                if not root:
                    res.append(None)
                    return 
                res.append(root.val)
                helper1(root.left,res)
                helper1(root.right,res)
            
            def helper2(root,res):
                if not root:
                    res.append(None)
                    return 
                res.append(root.val)
                helper2(root.right,res)
                helper2(root.left,res)

            helper1(cur.left,res1)
            helper2(cur.right,res2)
            if res1 == res2:
                return True
            else:
                return False