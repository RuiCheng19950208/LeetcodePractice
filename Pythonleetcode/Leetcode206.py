class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head1,head2):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans=ListNode()
        p1=head1
        p2=head2
        carry=0
        while p1 or p2 or carry==1:
            ans.next = ListNode()
            ans.val = carry
            if p1:
                ans.val+=p1.val
            if p2:
                ans.val+=p2.val
            carry=ans.val//10
            ans.val=ans.val%10
            print(ans.val)
            if p1:
                p1=p1.next
            if p2:
                p2=p2.next
        return ans

head1=ListNode(1)
head1.next=ListNode(1)
head1.next.next=ListNode(2)
head1.next.next.next=ListNode(3)

head2=ListNode(5)
head2.next=ListNode(1)
head2.next.next=ListNode(2)
head2.next.next.next=ListNode(9)
head2.next.next.next.next=ListNode(3)

print(Solution().reverseList(head1,head2))









# 修改val方法
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         pointer=head
#         val_list=[]
#         while pointer!=None:
#             val_list.append(pointer.val)
#             pointer=pointer.next
#         val_list=val_list[::-1]
#         pointer=head
#         p_index=0
#         while pointer!=None:
#             pointer.val=val_list[p_index]
#             pointer=pointer.next
#             p_index+=1
#         return head


# 三指针法
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head or not head.next:
#             return head
#         if not head.next.next:
#             first=head
#             second=head.next
#             first.next=None
#             second.next=first
#             head=second
#             return head
#         first=head
#         second=head.next
#         third=head.next.next
#         first.next=None
#         while third!=None:
#             second.next=first
#             first=second
#             second=third
#             third=third.next
#             # print(first.val,second.val,third.val)
#         second.next=first
#         head=second
#         return head












