class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False
        return p is q