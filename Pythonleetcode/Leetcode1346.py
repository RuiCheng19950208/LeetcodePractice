class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr=sorted(arr)
        for i in arr:
            if i!=0 and 2*i in arr:
                return True
            elif arr.count(0)>1:
                return True
        return False



print(Solution().checkIfExist(arr = [10,2,5,3]))
print(Solution().checkIfExist(arr = [7,1,14,11]))
print(Solution().checkIfExist( arr = [3,1,7,11]))