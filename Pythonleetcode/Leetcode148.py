class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Method 1 use list store val
# class Solution(object):
#     def sortList(self, head):
#         cur=head
#         val_list=[]
#         while cur:
#             val_list.append(cur.val)
#             cur=cur.next
#         val_list.sort()
#         cur=head
#         cur_index=0
#         for i in range(len(val_list)):
#             cur.val=val_list[cur_index]
#             cur_index+=1
#             cur=cur.next
#         return head

#Method 2 not use more space use the soluton from Leetcode147 is a good way
