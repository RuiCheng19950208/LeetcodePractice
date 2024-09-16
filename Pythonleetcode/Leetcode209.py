class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum_num=sum(nums)
        ans=10**5
        if sum_num<target:
            return 0
        temp_sum=nums[0]
        slow=0
        fast=0
        while slow<len(nums):
            if fast<len(nums)-1 and temp_sum<target:
                fast+=1
                temp_sum+=nums[fast]
            elif temp_sum<target:
                break
            elif temp_sum>=target:
                ans = min(ans, fast - slow + 1)
                temp_sum-=nums[slow]
                slow+=1
        return ans

print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(target = 4, nums = [1,4,4]))
print(Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))