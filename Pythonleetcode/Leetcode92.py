class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Val_list法
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        val_list=[]
        p_index=1
        p=head
        while p_index<=right:
            if p_index>=left:
                val_list.append(p.val)
            p_index+=1
            p=p.next
        val_list=val_list[::-1]
        val_index=0
        # print(val_list)
        p_index = 1
        p=head
        while p_index<=right:
            if p_index>=left:
                p.val=val_list[val_index]
                val_index+=1
            p_index+=1
            p=p.next
        return head


