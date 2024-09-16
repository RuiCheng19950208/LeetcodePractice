# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        target=root.val
        temp=[root]
        while len(temp)>0:
            a=temp.pop()
            if a.val!=target:
                return False
            if a.left:
                temp.append(a.left)
            if a.right:
                temp.append(a.right)

        return True