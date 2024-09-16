class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        a = head
        exist=[head]
        while True:
            a=a.next
            if a==None:
                return False
            else:
                if a in exist:
                    return True
                exist.append(a)


