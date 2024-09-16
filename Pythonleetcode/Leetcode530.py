class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
        val_list=[]
        temp_node=[root]
        while len(temp_node)>0:
            a=temp_node.pop()
            val_list.append(a.val)
            if a.right:
                temp_node.append(a.right)
            if a.left:
                temp_node.append(a.left)
        val_list.sort()
        ans=10**9
        for i in range(len(val_list)-1):
            k=abs(val_list[i+1]-val_list[i])
            if k<ans:
                ans=k
        return ans

