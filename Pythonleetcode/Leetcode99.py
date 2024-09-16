class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def helper(self,root,node_list):
        if not root:
            return
        self.helper(root.left,node_list)
        node_list.append(root)
        self.helper(root.right, node_list)


    def recoverTree(self, root):
        val_list=[]
        node_list=[]
        self.helper(root,node_list)
        for i in range(len(node_list)):
            val_list.append(node_list[i].val)
            val_list=sorted(val_list)
        for i in range(len(node_list)):
            node_list[i].val=val_list[i]



        return root


