class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res


