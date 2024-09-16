class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        target=int(sum(A)/3)
        if target!=sum(A)/3:
            return False
        i=0
        j=len(A)-1
        current_firstpart_sum=A[i]
        current_lastpart_sum=A[j]
        while i<j-1 and i<len(A)-2:
            # print([i,j])
            if current_firstpart_sum!=target:
                i +=1
                current_firstpart_sum +=A[i]
            elif current_lastpart_sum!=target:
                j -=1
                current_lastpart_sum += A[j]
            else:
                return True
        return False



print(Solution().canThreePartsEqualSum(A = [1,-1,1,-1]))
print(Solution().canThreePartsEqualSum(A = [0,2,1,-6,6,-7,9,1,2,0,1]))
print(Solution().canThreePartsEqualSum(A = [0,2,1,-6,6,7,9,-1,2,0,1]))
print(Solution().canThreePartsEqualSum(A = [3,3,6,5,-2,2,5,1,-9,4]))
print(Solution().canThreePartsEqualSum(A = [18,12,-18,18,-19,-1,10,10]))