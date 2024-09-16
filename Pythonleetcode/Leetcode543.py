class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def find_node_depth(node):
            if not node:
                return -1
            r=find_node_depth(node.left)
            l=find_node_depth(node.right)
            self.ans=max(self.ans,l+r+2)
            # print(self.ans)
            return 1 + max(r, l)
        if not root:
            return 0
        find_node_depth(root)

        return self.ans