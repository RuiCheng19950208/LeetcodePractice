class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def find_diff(self,node):
            if not node:
                return 0
            l=find_diff(self,node.left)
            r=find_diff(self,node.right)
            self.ans+=abs(l-r)

            return l+r+node.val

        find_diff(self,root)
        return self.ans
