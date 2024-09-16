class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First Approach pure ListNode
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        slow=ListNode(0, head)
        fast=head
        ans=slow
        while fast:
            slow=slow.next
            fast=fast.next
            if fast:
                while fast.val==slow.val:
                    fast=fast.next
                    if not fast:
                        break
            slow.next=fast
        return ans.next


# Second Approach: Vector and Set
# class Solution(object):
#     def deleteDuplicates(self, head):
#         node_val=[]
#         cur=head
#         while cur:
#             node_val.append(cur.val)
#             cur=cur.next
#         node_val=sorted(list(set(node_val)))
#         ans=ListNode()
#         cur=ans
#         for i in range(len(node_val)):
#             cur.next = ListNode(node_val[i])
#             cur=cur.next
#
#
#         return ans.next
#
