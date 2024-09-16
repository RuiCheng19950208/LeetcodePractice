class Solution(object):
    def findTargetSumWays(self, nums, S):

        T=(sum(nums)+S)
        print(T)
        if T%2!=0:
            return 0
        else:
            T=int(T/2)
        dp=[]
        zeros_num=0
        new_num=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zeros_num+=1
            else:
                new_num.append(nums[i])
        nums=new_num
        if len(nums)==1:
            if nums[0]==S or nums[0]==-S :
                return 1*(2**zeros_num)
            else:

                return 0
        if sum([abs(i) for i in nums])<S:
            return 0
        for i in range(len(nums)+1):
            dp.append([1]+[0]*T)
        # print(T,dp)
        for i in range(1,len(nums)+1):
            for j in range(1,T+1):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]

        # print(zeros_num,dp)
        return dp[-1][-1]*(2**zeros_num)

# print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3 ))
# print(Solution().findTargetSumWays([1,2,7,9,981], 1000000000))
# print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
# print(Solution().findTargetSumWays([1,0], 1))
print(Solution().findTargetSumWays([7,9,3,8,0,2,4,8,3,9], 0))




