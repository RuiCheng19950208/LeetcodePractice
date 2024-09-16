class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def helper(self,root,res):
        if not root:
            return None

        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)


    def inorderTraversal(self, root):
        self.res=[]
        self.helper(root,self.res)
        return self.res