class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Approach, we can use inorder search

class Solution(object):
    def helper(self, root,res):
        if not root:
            return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right, res)


    def isValidBST(self, root):
        res=[]
        self.helper(root,res)
        if res==sorted(res) and len(res)==len(list(set(res))):
            return True
        else:
            return False



# # Second Approach??
#
# class Solution(object):
#     def helper(self, root,res):