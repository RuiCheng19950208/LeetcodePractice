class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# # TimeLimite
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         curA=headA
#         curB=headB
#         nodeList=[]
#         while curA:
#             nodeList.append(curA)
#             curA=curA.next
#         nodeList.append(None)
#         while curB:
#             if curB in nodeList:
#                 return curB
#             else:
#                 curB=curB.next
#         return None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA=headA
        curB=headB
        while curA!=curB:
            if curA == None:
                curA = headB
            elif curA.next:
                curA=curA.next
            else:
                curA=None

            if curB == None:
                curB = headA
            elif curB.next:
                curB=curB.next
            else:
                curB=None

        return curA





