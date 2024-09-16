# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return 0
        ans=[]
        temp=[root]
        next_temp=[]
        while len(temp)>0:
            temp_sum=0
            for i in temp:
                temp_sum+=i.val
                if i.left:
                    next_temp.append(i.left)
                if i.right:
                    next_temp.append(i.right)
            ans.append(float(temp_sum)/len(temp))
            temp=next_temp
            next_temp=[]


        return ans[::-1]

