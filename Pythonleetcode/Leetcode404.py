class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return  0
        temp=[root]
        ans=0
        while len(temp)>0:
            a=temp.pop()
            if a.left:
                temp.append(a.left)
                if not a.left.left and not a.left.right:
                    ans+=a.left.val
            if a.right:
                temp.append(a.right)
        return ans


