# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans=[]
        def append_ans(root):
            if root.left!=None:
                append_ans(root.left)
            if root!=None:
                ans.append(root.val)
            if root.right!=None:
                append_ans(root.right)
        append_ans(root)


        result=TreeNode()
        temp=result
        temp.val=ans[0]
        if len(ans)>1:
            for i in range(1,len(ans)):
                temp.right=TreeNode()
                temp=temp.right
                temp.val=ans[i]

        return result

