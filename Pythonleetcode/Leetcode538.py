# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum=0
        def dfs(root):
            if not root:
                return
            else:
                dfs(root.right)
                root.val += self.sum
                self.sum=root.val
                dfs(root.left)
        dfs(root)
        return root


