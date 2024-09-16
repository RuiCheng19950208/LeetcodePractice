# class Solution(object):
#     def wiggleSort(self, nums):
#         nums=sorted(nums)
#         ans=[0]*len(nums)
#         small=nums[:int((len(nums)+1)/2)]
#         big = nums[int((len(nums) + 1) / 2):]
#         for i in range(len(small)):
#             ans[2*i]=small[i]
#
#         for i in range(len(big)):
#             ans[2 * i+1] = big[i]
#         for i in range(len(nums)):
#             nums[i]=ans[i]
#         print(nums)
# in-place原因被拒



# class Solution(object):
#     def wiggleSort(self, nums):
#         nums = sorted(nums)
#         for i in range(int((len(nums)+1)/2))[::-1]:
#
#             nums[i],nums[2*i]=nums[2*i],nums[i]
#第二种因为inplace被拒绝的正确方法










print(Solution().wiggleSort([1, 5, 1, 1, 6, 4]))
print(Solution().wiggleSort([1, 3, 2, 2, 3, 1]))
print(Solution().wiggleSort([1, 3, 2, 4, 5, 6,7]))