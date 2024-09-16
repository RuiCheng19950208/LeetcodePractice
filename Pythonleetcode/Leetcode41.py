class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        if  len(nums)==0 or nums[-1]<1:
            return 1
        target=1
        for i in range(len(nums)):
            # print(i,nums[i])
            if target<nums[i] and target!=1:
                return nums[i-1]+1
            elif target<nums[i] and target==1:
                return 1
            if target==nums[i]:
                target +=1
        return nums[-1]+1





print(Solution().firstMissingPositive([]))
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))
