class Solution:

    def maxSubArray(self, nums):


        length = len(nums)

        for i in range(1, length):


            subMaxSum = max(nums[i] + nums[i - 1], nums[i])

            nums[i] = subMaxSum



        return max(nums)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))