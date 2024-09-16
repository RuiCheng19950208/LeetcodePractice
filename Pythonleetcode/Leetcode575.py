class Solution(object):
    def distributeCandies(self, candies):

        b=list(set(candies))
        if len(b)>=len(candies)/2:
            return int(len(candies)/2)
        else:
            return int(len(b))







print(Solution().distributeCandies([1,1,2,2,3,3]))
print(Solution().distributeCandies([1,1,2,3]))
