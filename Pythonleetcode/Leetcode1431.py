class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        candies_sort=sorted(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=candies_sort[-1]:
                ans.append(True)
            else:
                ans.append(False)


        return ans






print(Solution().kidsWithCandies([4,2,1,1,2], 1))

print(Solution().kidsWithCandies([12,1,12],  10))


