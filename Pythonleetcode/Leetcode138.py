class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        dict={}
        ans=Node(0)
        cur_ans=ans
        cur_head=head
        dict[cur_head]=cur_ans

        while cur_head:
            cur_ans.val=cur_head.val
            if cur_head.next:
                cur_ans.next=Node(0)
            cur_head=cur_head.next
            cur_ans=cur_ans.next
            dict[cur_head]=cur_ans

        cur_ans=ans
        cur_head=head

        while cur_head:
            cur_ans.random=dict[cur_head.random]
            cur_head=cur_head.next
            cur_ans=cur_ans.next


        return ans
