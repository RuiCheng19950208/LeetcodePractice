class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # First Approach: pure ListNode
# class Solution(object):
#     def deleteDuplicates(self, head):
#         if not head:
#             return head
#         slow=ListNode(0,head)
#         mid=head
#         fast=head.next
#         ans=slow
#         while fast:
#             if mid.val==fast.val:
#                 while mid.val==fast.val:
#                     fast=fast.next
#                     if not fast:
#                         break
#                 slow.next=fast
#                 mid=fast
#                 if fast:
#                     fast=fast.next
#             else:
#                 slow=slow.next
#                 mid = mid.next
#                 fast=fast.next
#         return ans.next


# Second Approach: Dictionary

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        cur=head
        node_val_list=[]
        my_dict={}
        while cur:
            my_dict[cur.val]=my_dict.get(cur.val,0)+1
            cur=cur.next
        ans_list=[]
        for key in my_dict:
            if my_dict[key]==1:
                ans_list.append(key)
        ans_list=sorted(ans_list)
        ans=ListNode()
        cur=ans
        for i in range(len(ans_list)):
            cur.next=ListNode(ans_list[i])
            cur=cur.next
        return ans.next
