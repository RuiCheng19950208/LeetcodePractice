class Solution(object):
    def minCostClimbingStairs(self, cost):
        ans=cost[0:2]
        for i in range(2,len(cost)):
            ans.append(min((ans[-1]+cost[i]),(ans[-2]+cost[i])))
        return min(ans[-1],ans[-2])








print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
))