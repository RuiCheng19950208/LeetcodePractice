class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val_list=[]
        pointer=head
        while pointer!=None:
            val_list.append(pointer.val)
            pointer=pointer.next

        for i in range(len(val_list)//2):
            if val_list[i]!=val_list[-i-1]:
                return False
        return True
