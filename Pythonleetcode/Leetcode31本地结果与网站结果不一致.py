class Solution(object):
    def nextPermutation(self, nums):
        index1=-1
        while abs(index1)!=len(nums):
            index1 -=1
            if nums[index1] >= nums[index1+1]:
                continue
            else:
                for i in range(len(nums[index1+1:])):
                    if nums[-1-i]>nums[index1]:
                        nums[index1],nums[-1-i] = nums[-1-i],nums[index1]
                        nums[index1+1:]=sorted(nums[index1+1:])
                return  nums
        return nums[::-1]






print(Solution().nextPermutation([1,2,3]))
print(Solution().nextPermutation([3,2,1]))
print(Solution().nextPermutation([1,2]))
# print(Solution().nextPermutation([1,1,5]))
# print(Solution().nextPermutation([1,3,2]))
# print(Solution().nextPermutation([2,3,1]))
