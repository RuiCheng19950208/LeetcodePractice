# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(root):
            if not root:
                return 0
            else:
                return max(height(root.right), height(root.left)) + 1

        if not root:
            return True
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left) and abs(height(root.left)-height(root.right))<=1



