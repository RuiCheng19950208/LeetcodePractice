class Solution(object):
    def maximumWealth(self, accounts):
        ans=0
        for i in accounts:
            ans=max(ans,sum(i))

        return ans

print(Solution().maximumWealth( accounts = [[1,2,3],[3,2,1]]))
print(Solution().maximumWealth( accounts = [[1,5],[7,3],[3,5]]))