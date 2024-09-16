# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def merge(r1,r2):
            if r1==None and r2==None:
                return
            elif r1==None:
                return r2

            elif r2==None:
                return r1
            else:
                r1.val+=r2.val
                r1.left=merge(r1.left , r2.left)
                r1.right=merge(r1.right, r2.right)
                return r1
        merge(root1,root2)
        return root1
