class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        choice=len(piles)//3
        ans=0
        choice_index=0
        for i in range(len(piles)-2,-2,-2):
            choice_index+=1
            ans+=piles[i]
            if choice_index==choice:
                break
        return ans

print(Solution().maxCoins([2,4,1,2,7,8]))
print(Solution().maxCoins([2,4,5]))