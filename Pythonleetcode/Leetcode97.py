class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):
            return False

        dp=[[False for i in range(len(s1)+1)]for i in range(len(s2)+1)]
        dp[0][0]=True
        for i in range(len(s1)):
            if s3[i]==s1[i]:
                dp[0][i+1]=True
            else:
                break
        for i in range(len(s2)):
            if s3[i]==s2[i]:
                dp[i+1][0]=True
            else:
                break

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s3[i+j-1]==s1[j-1]:
                    if dp[i][j-1]==True:
                        dp[i][j]=True
                if s3[i+j-1]==s2[i-1]:
                    if dp[i-1][j]==True:
                        dp[i][j]=True
        # print(dp)


        return dp[-1][-1]



print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print(Solution().isInterleave(s1 = "aabc", s2 = "abad", s3 = "aabadabc"))



