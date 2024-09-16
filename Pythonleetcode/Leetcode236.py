class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root==None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        L=self.lowestCommonAncestor(root.left,p,q)
        R=self.lowestCommonAncestor(root.right,p,q)

        if R!=None and L!=None:
            return root
        elif  L!=None:
            return  L
        elif  R!=None:
            return  R
        return None
