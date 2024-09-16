class Solution(object):
    def countBinarySubstrings(self, s):
        if len(s)==1 or len(s)==0:
            return 0

        count=[]
        cou=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cou=cou+1
            else:
                count.append(cou)
                cou=1
        count.append(cou)


        ans=0
        for i in range(1,len(count)):
            ans=ans+min(count[i],count[i-1])
        return ans







print(Solution().countBinarySubstrings("00110011"))
print(Solution().countBinarySubstrings("10101"))
