class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        len_list=0
        len_pointer = head
        fast_pointer = head
        slow_pointer =head
        while len_pointer!=None:
            len_pointer=len_pointer.next
            len_list+=1

        k=k%len_list
        while k>0:
            fast_pointer=fast_pointer.next
            k-=1
        while fast_pointer.next!=None:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        fast_pointer.next=head
        head=slow_pointer.next
        slow_pointer.next=None
        return head
