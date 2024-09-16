class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf(node):
            ans=[]

            if not node:
                return ans
            temp = [node]
            while len(temp)>0:
                a=temp.pop()
                if not a.left and not a.right:
                    ans.append(a.val)
                if a.left:
                    temp.append(a.left)
                if a.right:
                    temp.append(a.right)
            return ans
        leafs1=get_leaf(root1)
        leafs2=get_leaf(root2)
        if leafs1==leafs2:
            return True
        else:
            return False