# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans=0
        def sum_all_node(self,node):
            if node==None:
                return
            if node.val<=high and node.val>=low:
                self.ans += node.val
            sum_all_node(self,node.left)
            sum_all_node(self, node.right)
            return
        sum_all_node(self,root)
        return self.ans
