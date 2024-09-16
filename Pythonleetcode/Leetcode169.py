class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        for i in set(nums):
            n=0
            for j in range(len(nums)):
                if i==nums[j]:
                    n=n+1
                if n>len(nums)/2:
                    return i




print(Solution().majorityElement([2,2,1,1,2,2]))