import list
class Solution(object):

    def swapPairs(self, head):

        if head == None:
            return head

        cur = ListNode(0)

        cur.next = head

        first = cur

        while cur.next and cur.next.next:
            n1 = cur.next

            n2 = n1.next

            nxt = n2.next

            n1.next = nxt

            n2.next = n1

            cur.next = n2

            cur = n1

        return first.next


print(Solution().swapPairs([1,2,3,4]))