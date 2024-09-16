# Definition for a binary tree node.


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans_dict={}
        def get_ans_dict(node):
            if node==None:
                return
            if node.val not in ans_dict.keys():
                ans_dict[node.val] = 1
            else:
                ans_dict[node.val] += 1
            get_ans_dict(node.left)
            get_ans_dict(node.right)

        get_ans_dict(root)
        ans=[]
        temp=0
        for i in ans_dict:
            if ans_dict[i]>temp:
                ans=[i]
                temp=ans_dict[i]
            elif ans_dict[i]==temp:
                ans.append(i)
        return ans


