class Solution(object):
    def heightChecker(self, heights):
        sorted_h=sorted(heights)
        ans=0
        for i in range(len(heights)):
            if sorted_h[i]!=heights[i]:
                ans+=1


        return ans

print(Solution().heightChecker([1,1,4,2,1,3]))
print(Solution().heightChecker([5,1,2,3,4]))