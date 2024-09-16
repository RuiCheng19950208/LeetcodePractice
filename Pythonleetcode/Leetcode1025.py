class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N==1:
            return False
        if N==2:
            return True
        dp=[False for i in range(N+1)]
        dp[2]=True
        for i in range(N+1):
            for j in range(1,i):
                if i%j==0 and dp[i-j]==False:
                    dp[i]=True
                break
        return dp[-1]


print(Solution().divisorGame(2))
print(Solution().divisorGame(3))
print(Solution().divisorGame(4))
print(Solution().divisorGame(10))
