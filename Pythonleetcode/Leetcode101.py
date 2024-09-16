class Solution(object):
    def recurrent(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None or left.val!=right.val:
            return False
        else:
            return self.recurrent(left.left, right.right) and  self.recurrent(left.right, right.left)

    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.recurrent(root.left, root.right)

