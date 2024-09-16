
#超出时间限制
# class Solution(object):
#     def threeSum(self, nums):
#         ans=[]
#         nums.sort()
#         print(nums)
#         for i in range(1,len(nums)-1):
#             for j in range(0,i):
#                 for k in range(i+1,len(nums)):
#
#                     if nums[i]+nums[j]+nums[k]==0 and [nums[j],nums[i],nums[k]]not in ans:
#                         ans.append([nums[j],nums[i],nums[k]])
#                         print([j, i, k])
#         return ans


class Solution:

    def threeSum(self, nums):

        nums.sort()

        res = []

        i = 0

        for i in range(len(nums)):

            if i == 0 or nums[i] > nums[i - 1]:

                l = i + 1

                r = len(nums) - 1

                while l < r:

                    s = nums[i] + nums[l] + nums[r]

                    if s == 0:

                        res.append([nums[i], nums[l], nums[r]])

                        l += 1

                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1

                    elif s > 0:

                        r -= 1

                    else:

                        l += 1

        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))