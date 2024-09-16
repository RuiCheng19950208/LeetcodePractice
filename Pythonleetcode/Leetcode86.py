class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        right_dummy = ListNode()
        left_dummy = ListNode()
        r = right_dummy
        l = left_dummy
        pointer = head
        while pointer != None:
            temp=ListNode(pointer.val)
            if pointer.val < x:
                l.next=temp
                l=l.next
            else:
                r.next = temp
                r = r.next
            pointer = pointer.next
            l.next = right_dummy.next

        return left_dummy.next