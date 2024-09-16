class Solution(object):
    def largestAltitude(self, gain):
        ans=[0]
        for i in gain:
            ans.append(ans[-1]+i)
        return max(ans)

print(Solution().largestAltitude( [-5,1,5,0,-7]))
print(Solution().largestAltitude( [-4,-3,-2,-1,4,3,2]))