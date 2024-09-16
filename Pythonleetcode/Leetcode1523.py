class Solution(object):
    def countOdds(self, low, high):
        ans=0
        mod_two=(high-low)//2
        remainder=(high-low)%2
        if(remainder==0):
            if(low%2==0):
                return mod_two
            else:
                return mod_two+1

        else:
            return mod_two+1





print(Solution().countOdds(3,7))
print(Solution().countOdds(8,10))
print(Solution().countOdds(4,7))