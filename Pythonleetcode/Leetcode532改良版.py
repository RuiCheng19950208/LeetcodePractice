class Solution(object):
    def findPairs(self, nums, k):
        if len(nums)==0 or len(nums)==1:
            return 0
        count=0
        if k<0:
            return count
        elif k==0:
            nums1=list(set(nums))

            if len(nums1)==1:
                return 1
            for i in range(len(nums1)):

                if nums.count(nums1[i])>1:
                    count=count+1
            return count
        else:
            nu=[]
            nums1=sorted(list(set(nums)))
            for i in range(len(nums1)):
                nu.append(nums1[i])
            for i in range(len(nums1)):
                if nums1[i]+k in nu:
                    count=count+1




            return count






print(Solution().findPairs([3, 1, 4, 1, 5], 2))
print(Solution().findPairs([1, 2, 3, 4, 5], 1))
print(Solution().findPairs([1, 3, 1, 5, 4], 0))
print(Solution().findPairs([1, 2,3,4,5], 3))
print(Solution().findPairs([3,1,4,1,5],2))
print(Solution().findPairs([1,1,1,2,2],0))
