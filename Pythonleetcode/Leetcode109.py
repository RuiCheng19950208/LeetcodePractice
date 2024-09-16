class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):

    def helper(self,start,end):
        if start==end:
            return None
        slow=start
        fast=start
        while fast!=end and fast.next!=end:
            print(slow.val,fast.val)
            fast=fast.next.next
            slow=slow.next

        root=TreeNode(slow.val)
        root.left = self.helper(start,slow)
        root.right = self.helper(slow.next,end)
        return root

    def sortedListToBST(self, head):
        return self.helper(head,None)

