class Solution(object):
    def lastStoneWeightII(self, stones):
        T=sum(stones)
        if T%2==0:
            ans_fix=0
        else:
            ans_fix=1
        T = T // 2
        print(T)
        dp=[]
        for i in range(len(stones)+1):
            dp.append([True]+[False]*T)

        for i in range(1,len(stones) + 1):
            for j in range(1,T+1):
                if j-stones[i-1]>=0:
                    dp[i][j]=(dp[i-1][j] or dp[i-1][j-stones[i-1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        ans_index=0
        for i in dp[-1][::-1]:
            if i==True:
                break
            else:
                ans_index+=1
        return 2*ans_index+ans_fix

print(Solution().lastStoneWeightII([2,7,4,1,8,1]))