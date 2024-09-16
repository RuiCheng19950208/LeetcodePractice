# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.list=[]

        for i in lists:
            curr=i
            while curr.next:
                self.list.append(curr.val)
                curr=curr.next
        self.list=sorted(self.list)
        res_index=0
        curr=self.res = ListNode(0)
        # print(self.list)
        while res_index<len(self.list):
            curr.next=ListNode(self.list[res_index])
            curr=curr.next
            res_index +=1
        return self.res.next


