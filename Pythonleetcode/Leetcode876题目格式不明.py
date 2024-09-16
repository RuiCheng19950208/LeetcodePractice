class Solution(object):
    def middleNode(self, head):
        if len(head)%2==1:
            return head[(int(len(head)/2)):]
        else:
            return head[int(len(head)/2):]






print(Solution().middleNode([1,2,3,4,5]))

print(Solution().middleNode([1,2,3,4,5,6]))