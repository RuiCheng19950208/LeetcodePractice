# 超时
# class Solution(object):
#     def rotate(self, nums, k):
#         def right(nums):
#             nums[0],nums[-1]=nums[-1],nums[0]
#             for i in range(0,len(nums)-2):
#                 nums[-i-1],nums[-i-2]=nums[-i-2],nums[-i-1]
#
#
#         if len(nums)==0 or k==0:
#             return nums
#
#
#
#         for i in range(k):
#             right(nums)
#             print(nums)
#
#         return nums


class Solution(object):

    def rotate(self, nums, k):




        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]

        return nums

print(Solution().rotate([1,2,3,4,5,6,7],3))





