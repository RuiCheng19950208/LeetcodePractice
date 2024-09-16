class Solution(object):
    def singleNumber(self, nums):
        ans=[]
        nums.sort()
        if len(nums)==2:
            return nums
        if nums[0]!=nums[1]:
            ans.append(nums[0])
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            ans.append(nums[len(nums)-1])
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                ans.append(nums[i])
            if len(ans)==2:
                return ans





print(Solution().singleNumber([1,2,1,3,2,5]))