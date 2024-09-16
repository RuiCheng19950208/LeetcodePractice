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
        if root.val<q.val and root.val<p.val:
            if root.right:
                return self.lowestCommonAncestor(root.right,p,q)
        if root.val > q.val and root.val > p.val:
            if root.left:
                return self.lowestCommonAncestor(root.left, p, q)
        return root