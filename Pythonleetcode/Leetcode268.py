class Solution(object):
    def missingNumber(self, nums):


        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i]==2:
                return nums[i]+1
        if max(nums)==len(nums):
            return 0
        else: return len(nums)



print(Solution().missingNumber([3,0,1]))