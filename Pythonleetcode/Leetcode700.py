# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#网络资料给出的标准答案，利用BST数据分布规律
class Solution(object):
    def searchBST(self, root, val):
        if root.val == val:
            return root
        if val > root.val and root.right != None:
            return self.searchBST(root.right, val)
        elif val < root.val and root.left != None:
            return self.searchBST(root.left, val)

#以下是一个没有运用BST数据分布规律的普适方法（程睿自己想出来的）
# class Solution(object):
#     def searchBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#
#         def find_node(node):
#             temp=None
#             if node.val==val:
#                 return node
#             if node.left!=None:
#                 temp=find_node(node.left)
#                 if temp!=None:
#                     return temp
#             if node.right!=None and temp ==None:
#                 return find_node(node.right)
#             return None
#         ans=find_node(root)
#         return ans
