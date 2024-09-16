class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        if  not head or not head.next:
            return head
        slow=ListNode(0,head)
        mid=head
        fast=head.next
        ans = slow
        while fast and mid:
            slow.next = fast
            mid.next = fast.next
            fast.next = mid

            if not mid.next:
                break
            elif not mid.next.next:
                break
            else:
                fast=mid.next.next
                mid=mid.next
                slow=slow.next.next
            # print(slow.val,mid.val,fast.val)
        return ans.next

