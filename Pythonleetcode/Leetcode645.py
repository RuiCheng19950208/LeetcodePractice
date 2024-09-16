class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        set_nums=list(set(nums))
        nums_compare=[i for i in range(1,len(nums)+1)]
        dup=0
        miss=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                dup=nums[i]
                break
        for i in range(len(nums) - 1):
            if nums_compare[i] != set_nums[i]:
                miss = nums_compare[i]
                break

        if miss==0:
            miss=nums_compare[-1]
        return [dup,miss]



print(Solution().findErrorNums( nums = [1,2,2,4]))
print(Solution().findErrorNums( nums = [1,1]))
print(Solution().findErrorNums( nums = [2,2]))
print(Solution().findErrorNums( nums = [3,2,3,4,6,5]))
print(Solution().findErrorNums( nums = [1,5,3,2,2,7,6,4,8,9]))



