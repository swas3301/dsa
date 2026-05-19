"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res =[]
        def trav(node):
            if not node:
                return 
            for i in node.children:
                trav(i)
            res.append(node.val)
        
        trav(root)
        return res
