class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """

        for i in range(len(arr)):
            pattern=arr[i:i+m]
            count=0
            for j in range(i,len(arr),m):
                # print([i,j],pattern)
                if arr[j:j+m]==pattern:
                    count +=1
                else:
                    break
                if count==k:
                    return  True

        return False



print(Solution().containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
print(Solution().containsPattern( arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
print(Solution().containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))
print(Solution().containsPattern(arr = [1,2,3,1,2], m = 2, k = 2))
print(Solution().containsPattern(arr = [2,2,2,2], m = 2, k = 3))
print(Solution().containsPattern([2,2,1,2,2,1,1,1,2,1],2,2))