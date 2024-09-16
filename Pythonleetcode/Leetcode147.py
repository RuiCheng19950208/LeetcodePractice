class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        cur=head
        while cur.next:
            if cur.val<=cur.next.val:
                cur=cur.next
            else:
                pre=dummy
                temp=cur.next
                cur.next=cur.next.next
                while True:
                    if pre.next.val>temp.val:
                        temp.next=pre.next
                        pre.next=temp
                        break
                    else:
                        pre=pre.next

        return dummy.next
