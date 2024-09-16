class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()

        if len(nums)==1 or len(nums)==0:
            return 0

        i = 0
        j = 1
        count = 0
        result=[]

        while(1):

            if j+i==2*len(nums)-2:
                break

            if nums[j]-nums[i]<k and j==len(nums)-1:
                break
            elif  nums[j]-nums[i]==k and j-i==1 :
                if [nums[i],nums[j]] not in result:
                    result.append([nums[i], nums[j]])
                    count = count + 1
                    j = j + 1
                else:
                    j = j + 1
            elif nums[j] - nums[i] == k and j - i > 1 :
                if [nums[i], nums[j]] not in result:
                    result.append([nums[i], nums[j]])
                    count = count + 1
                    i = i + 1
                else:
                    i = i + 1

            elif nums[j]-nums[i]<k:
                j=j+1

            elif nums[j]-nums[i]>k and j-i>1:
                i=i+1

            elif nums[j]-nums[i]>k and j-i==1:
                j=j+1

        return count








print(Solution().findPairs([3, 1, 4, 1, 5], 2))
print(Solution().findPairs([1, 2, 3, 4, 5], 1))
print(Solution().findPairs([1, 3, 1, 5, 4], 0))
print(Solution().findPairs([1, 2,3,4,5], 3))
print(Solution().findPairs([3,1,4,1,5],2))