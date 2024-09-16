class Solution(object):
    def rob(self, nums):

        def dp_helper(nums):
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums[0], nums[1])
            else:
                dp = [0] * len(nums)
                dp[0] = nums[0]
                dp[1] = max(nums[0], nums[1])
                for i in range(2, len(nums)):
                    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # print(dp)
            return dp[-1]

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        return max(dp_helper(nums[1:]),dp_helper(nums[:len(nums)-1]))


print(Solution().rob([2, 3, 2]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([1,3,1,3,100]))