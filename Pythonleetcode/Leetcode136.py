# Approach 1
# class Solution(object):
#     def singleNumber(self, nums):
#         nums.sort()
#         if len(nums)==1:
#             return nums[0]
#         if nums[0]!=nums[1]:
#             return nums[0]
#         if nums[len(nums)-1]!=nums[len(nums)-2]:
#             return nums[len(nums)-1]
#
#         for i in range(1,len(nums)-1):
#             if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
#                 return nums[i]

#Approach 2
class Solution(object):
    def singleNumber(self, nums):
        dict={}
        for i in nums:
            dict[i]= dict.get(i,0)+1
        for i in dict:
            if dict[i]==1:
                return i


print(Solution().singleNumber([1,2,4,1,2]))