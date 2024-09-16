class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        a=head
        exist_node_list=[]
        while a!=None:
            if a in exist_node_list:
                return a
            exist_node_list.append(a)
            a = a.next
        return None

