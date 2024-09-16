class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        while len(stones)>1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-1]-=stones[-2]
                stones.pop(-2)
            stones.sort()
        if len(stones)==0:
            return 0
        else:
            return stones[0]

print(Solution().lastStoneWeight([2,7,4,1,8,1]))