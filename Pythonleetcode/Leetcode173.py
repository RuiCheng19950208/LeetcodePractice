class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.res=[]
        self.i=-1
        self.helper(root)


    def next(self):
        """
        :rtype: int
        """
        self.i+=1
        return self.res[self.i]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i<len(self.res)-1:
            return True
        else:
            return False
    def helper(self,root):
        if not root:
            return
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)