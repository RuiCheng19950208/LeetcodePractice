class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return False
        val_list=[]
        temp_node=[root]
        while len(temp_node)>0:
            a=temp_node.pop()
            val_list.append(a.val)
            if a.left:
                temp_node.append(a.left)
            if a.right:
                temp_node.append(a.right)
        for i in range(len(val_list)):
            if k-val_list[i] in val_list[:i]+val_list[i+1:]:
                return True
        return False