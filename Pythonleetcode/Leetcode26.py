class Solution(object):
    def removeDuplicates(self, nums):
        x=[]
        for i in range(0,len(nums)):
            if i==0:
                x.append(nums[i])

            elif nums[i]!=nums[i-1]:
                x.append(nums[i])

        nums[:] =x


        return len(x)

print (Solution().removeDuplicates([1,1,2,2,2]))




# class Solution(object):
#     def removeDuplicates(self, nums):
#                 newTail=0
#                 if not nums:
#                     return 0
#
#                 index = 0
#
#                 for i in range(1, len(nums)):
#                     if nums[i] != nums[newTail]:
#                         newTail += 1
#                         nums[newTail] = nums[i]
#
#                 return newTail + 1