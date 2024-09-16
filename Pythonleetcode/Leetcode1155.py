# class Solution(object):
#     def numRollsToTarget(self, d, f, target):
#         ans=0
#         def dp( d, f, target):
#             if d == 1 and target <= f:
#                 return 1
#             elif d == 1:
#                 return 0
#             else:
#                 result=0
#                 for i in range(1,f):
#                     result += dp( d-1, f, target-i)
#                 return result
#
#         if d == 1 and target <= f:
#             return 1
#         elif d == 1:
#             return 0
#         else:
#             for i in range(1,f+1):
#                 ans += dp(d - 1, f, target - i)
#
#
#         return ans


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """

        if d * f < target or d > target:
            return 0

        if d == 1:
            if target <= f:
                return 1
            else:
                return 0
        M = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):

                if j == 1:
                    dp[i][j] = dp[i - 1][0]
                elif j <= f:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] - dp[i - 1][j - f - 1])

        return dp[d][target] % M



print(Solution().numRollsToTarget(d = 1, f = 6, target = 3))
print(Solution().numRollsToTarget(d = 2, f = 6, target = 7))
print(Solution().numRollsToTarget(d = 2, f = 5, target = 10))
print(Solution().numRollsToTarget( d = 1, f = 2, target = 3))
print(Solution().numRollsToTarget( d = 30, f = 30, target = 500))