class Solution(object):
    def containsDuplicate(self, nums):
        return len(list(set(nums)))!=len(nums)



print(Solution().containsDuplicate([1,2,3,1]))