# import copy
# class Solution(object):
#     def sortColors(self, nums):
#         ans=[1]*len(nums)
#         j=0
#         k=len(nums)-1
#         for i in range(0,len(nums)):
#             if nums[i]==0:
#                 ans[j]=0
#                 j=j+1
#             if nums[i]==2:
#                 ans[k] = 2
#                 k = k -1
#         print(ans)


class Solution(object):
    def sortColors(self, nums):
        nums.sort()


class Solution(object):
    def sortColors(self, nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums


print(Solution().sortColors([2,0,2,1,1,0]))