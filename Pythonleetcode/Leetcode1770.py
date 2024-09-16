# DFS方法超时
class Solution(object):
    def maximumScore(self, nums, multipliers):
        last_index=len(nums)-1
        def dfs(r,l):
            k=l+last_index-r
            # print(r, l, k)
            if k==len(multipliers):
                return 0
            else:
                return max(dfs(r-1,l)+nums[r]*multipliers[k],dfs(r,l+1)+nums[l]*multipliers[k])
        return dfs(len(nums)-1,0)

# 参考答案：没看出来和第一种有什么区别，但它更快（可能是if dp[l][i]==0减少了重复计算）
# class Solution(object):
#     def maximumScore(self, nums, multipliers):
#         dp = [[0 for x in range(len(multipliers))] for y in range(len(multipliers))]
#         def dfs(l,i):
#             if i >= len(multipliers):
#                 return 0
#             if dp[l][i]==0:
#                 r = len(nums) - 1 - (i - l)
#                 dp[l][i] = max(nums[l] * multipliers[i] + dfs(l + 1, i + 1), nums[r] * multipliers[i] + dfs(l, i + 1))
#                 print(dp)
#             return dp[l][i]
#         return dfs(0, 0)


# class Solution(object):
#     def maximumScore(self, nums, multipliers):
#         dp = [[[0 for x in range(len(multipliers))] for y in range(len(multipliers))] for _ in range(len(multipliers)+1)]
#         i=0
#         j=-1
#         for k in range(len(multipliers)):
#             dp[k][i][j]=max(dp[k+1][i+1][j]+nums[i]*multipliers[k],dp[k+1][i][j-1]+nums[j]*multipliers[k])
#
#         return dp[0][0][len(multipliers)-1]



print(Solution().maximumScore( nums = [1,2,3], multipliers = [3,2,1]))
print(Solution().maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]))