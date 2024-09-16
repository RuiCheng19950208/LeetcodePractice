class Solution(object):
    def minCostToMoveChips(self, position):
        even_amount=0
        odd_amount=0
        for i in position:
            if (i%2==0):
                even_amount += 1
            else:
                odd_amount+=1
        return min(even_amount,odd_amount)



print(Solution().minCostToMoveChips([1,2,3]))
print(Solution().minCostToMoveChips([2,2,2,3,3]))
print(Solution().minCostToMoveChips([1,1000000]))



