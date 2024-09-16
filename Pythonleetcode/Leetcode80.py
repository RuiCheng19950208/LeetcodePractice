class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        fast=2
        slow=2
        while fast<len(nums):
            if nums[fast]!=nums[slow-2]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
            # print(slow,fast,nums)
        return slow


print(Solution().removeDuplicates( nums = [1,1,1,2,2,3]))
print(Solution().removeDuplicates( nums = [0,0,1,1,1,1,2,3,3]))
print(Solution().removeDuplicates( nums = [1,1,1]))
print(Solution().removeDuplicates( nums = [1,1,1,1]))
print(Solution().removeDuplicates( nums = [1,2,2]))
print(Solution().removeDuplicates( nums = [1,2,2,2]))



