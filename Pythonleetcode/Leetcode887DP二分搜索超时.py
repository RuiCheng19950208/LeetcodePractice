class Solution(object):
    def superEggDrop(self, K, N):
        if K>N:
            K=N+0
        dp=[]
        for i in range(K+1):
            dp.append([0]*(N+1))
        if K==0:
            return dp[0][-1]
        for j in range(1,N+1):
            dp[1][j]=j
        if K==1:
            return dp[1][-1]

        #二分搜索，依然超时
        if K>=2:
            for i in range(2,K + 1):
                for j in range(1, N + 1):
                    if i>j:
                        dp[i][j]=dp[j][j]
                    else:
                        up_limit=j+0
                        low_limit=1

                        while low_limit<=up_limit:
                            middle_index = low_limit + int((up_limit - low_limit) / 2)

                            broke=dp[i-1][middle_index-1]
                            nonbroke=dp[i][j-middle_index]
                            if nonbroke<broke:
                                up_limit=middle_index-1
                            else:
                                low_limit=middle_index+1

                            # print(i, j, middle_index, low_limit, up_limit)
                            # print(middle_index)
                        # dp[i][j] =min(max(dp[i-1][up_limit-1],dp[i][j-up_limit]),max(dp[i-1][low_limit-1],dp[i][j-low_limit]))+1
                        middle_index = low_limit + int((up_limit - low_limit - 1) / 2)
                        dp[i][j]=max(dp[i-1][middle_index-1],dp[i][j-middle_index])+1
        #以下循环时间复杂度较高
        # if K>=2:
        #     for i in range(2,K + 1):
        #         for j in range(1, N + 1):
        #             if i>j:
        #                 dp[i][j]=dp[j][j]
        #             else:
        #                 dp[i][j]=min([max([dp[i][j-k],dp[i-1][k-1]])+1 for k in range(1,j+1)])
        # print(dp)
        return dp[-1][-1]

print(Solution().superEggDrop(1,2))
print(Solution().superEggDrop(2,6))
print(Solution().superEggDrop(3,14))
print(Solution().superEggDrop(4,5000))
print(Solution().superEggDrop(11,8000))