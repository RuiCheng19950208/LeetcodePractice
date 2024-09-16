class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)
