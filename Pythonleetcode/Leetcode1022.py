# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if  not root.left and not root.right:
            if root.val==0:
                return 0
            else:
                return 1

        temp=[root]
        leaf_list=[]
        while len(temp)>0:
            a=temp.pop(0)
            if a.left:
                a.left.val=str(a.val)+str(a.left.val)
                temp.append(a.left)
            if a.right:
                a.right.val = str(a.val)+str(a.right.val)
                temp.append(a.right)
            if not a.right and not a.left:
                leaf_list.append(a.val)
        # print(leaf_list)


        return sum([int(i,2) for i in leaf_list])

