class Solution(object):
    def titleToNumber(self, s):
        ans=0
        value_base=ord("A")
        for i in range(len(s)-1,-1,-1):
            ans=(26**(len(s)-1-i))*(ord(s[i])-value_base+1)+ans
            print(i, s[i],ans)

        return ans




print(Solution().titleToNumber("AB"))

