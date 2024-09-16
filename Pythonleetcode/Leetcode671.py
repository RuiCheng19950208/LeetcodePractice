class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left and not root.right:
            return -1

        root_value=root.val
        temp_nodes=[root]

        val_list = []

        while len(temp_nodes)>0:
            a=temp_nodes.pop()
            if a.left:
                temp_nodes.append(a.left)
                temp_nodes.append(a.right)
                val_list.append(a.left.val)
                val_list.append(a.right.val)
        val_list.sort()
        for i in val_list:
            if i>root_value:
                return i


        return -1
