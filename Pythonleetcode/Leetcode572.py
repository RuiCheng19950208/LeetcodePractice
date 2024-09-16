# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def has_same_part(node,t):
            if node==None and t==None:
                return True
            elif node==None or t==None:
                return False
            elif node.val==t.val:
                print(node.left,t.left)
                return  has_same_part(node.right,t.right) and has_same_part(node.left,t.left)
            else:
                return False
        # print(s,t)

        if s==None:
            return False
        if has_same_part(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
