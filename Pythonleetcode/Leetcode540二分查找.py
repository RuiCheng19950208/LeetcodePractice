class Solution(object):
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid % 2 == 0:
                mid += 1
            if nums[mid] == nums[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1

        return nums[low]



# class Solution(object):
#     def singleNonDuplicate(self, nums):
#         num_set = list(set(nums))
#         for each in num_set:
#             if nums.count(each) == 1:
#                 return each
#暴力破解也可以通过





print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))