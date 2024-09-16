# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_num(root):
            if not root:
                return 0
            return root.val+10*get_num(root.next)

        sum_result=get_num(l1)+get_num(l2)
        str_sum_result=str(sum_result)
        len_result=len(str(sum_result))
        add_index=len_result-1
        ans_link = ListNode(0)
        p=ans_link
        while add_index>=0:
            p.next=ListNode(int(str_sum_result[add_index]))
            add_index -=1
            p=p.next

        return ans_link.next


