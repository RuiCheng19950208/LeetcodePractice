class Solution(object):
    def balancedStringSplit(self, s):
        temp_r=0
        temp_l=0
        ans=0
        for i in s:
            if i=='R':
                temp_r+=1
            else:
                temp_l+=1
            if temp_l==temp_r and temp_l!=0:
                ans+=1

        return ans

print(Solution().balancedStringSplit("RLRRLLRLRL"))
print(Solution().balancedStringSplit("RLLLLRRRLR"))
print(Solution().balancedStringSplit("LLLLRRRR"))
print(Solution().balancedStringSplit("RLRRRLLRLL"))