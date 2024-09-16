# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# One approach
# class Solution(object):
#     def calculate_depth(self,left,right,depth):
#         if left is None and right is None:
#             return depth
#         elif left is None :
#             return self.calculate_depth(right.left, right.right, depth + 1)
#         elif right is None:
#             return self.calculate_depth(left.left,left.right,depth+1)
#         # if (left.left is None and left.right is None) or (right.left is None and right.right is None):
#         #     return depth+1
#         else:
#             return min(self.calculate_depth(left.left,left.right,depth+1),self.calculate_depth(right.left,right.right,depth+1))
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         else:
#             depth=1
#             return self.calculate_depth(root.left,root.right,depth)


# Two approach


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.right and root.left:
            return min(self.minDepth(root.right),self.minDepth(root.left))+1
        else:
            return max(self.minDepth(root.right),self.minDepth(root.left))+1
