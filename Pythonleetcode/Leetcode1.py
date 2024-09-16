# # Approach 1
# class Solution(object):
#     def twoSum(self,nums, target):
#         for i, num in enumerate(nums):
#             sub_num = target - num
#             if sub_num in nums:
#                 index1 = nums.index(sub_num)
#                 if index1 != i:
#                     return [i, index1]

# Approach 2
class Solution(object):
    def twoSum(self,nums, target):
        for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                index1 = nums.index(sub_num)
                if index1 != i:
                    return [i, index1]

print(Solution().twoSum([2,0,17, 7, 11, 15],9))