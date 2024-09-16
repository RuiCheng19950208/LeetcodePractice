class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def helper(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left,res)
        self.helper(root.right, res)


    def preorderTraversal(self, root):
        res=[]
        self.helper(root,res)
        return res

