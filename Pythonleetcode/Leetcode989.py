class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        ans=[]
        num_A=0
        for i in range(len(A)):
            num_A = num_A*10+A[i]

        sum_result=num_A+K

        str_result=str(sum_result)

        for i in str_result:
            ans.append(int(i))
        return ans



print(Solution().addToArrayForm( A = [1,2,0,0], K = 34))
print(Solution().addToArrayForm( A = [2,7,4], K = 181))
print(Solution().addToArrayForm(A = [2,1,5], K = 806))
print(Solution().addToArrayForm(A = [9,9,9,9,9,9,9,9,9,9], K = 1))
