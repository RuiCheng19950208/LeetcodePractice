class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums)==1:
            return 0
        if sorted(nums)==nums:
            return 0

        while(1):
            if min(nums)!=nums[0] and max(nums)!=nums[-1]:
                return len(nums)
            if max(nums)==nums[-1]:
                nums.pop(-1)
            elif min(nums)==nums[0]:
                nums.pop(0)
            if len(nums)==0:
                return 0




print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(Solution().findUnsortedSubarray([1,2,3,3,3]))
