class Solution(object):
    def integerReplacement(self, n):
        if n==1:
            return 0
        dp=[n]
        step=0
        while True:
            # print(dp)
            need_to_append=[]
            for i in range(len(dp)):
                if dp[i]==1:
                    return step
                if dp[i]%2==1:
                    need_to_append.append(dp[i] + 1)
                    dp[i]-=1

                else:
                    dp[i]=dp[i]//2
            dp +=need_to_append
            step +=1





print(Solution().integerReplacement(8))
print(Solution().integerReplacement(7))
print(Solution().integerReplacement(4))