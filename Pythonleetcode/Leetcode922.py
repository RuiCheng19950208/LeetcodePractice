class Solution(object):
    def sortArrayByParityII(self, A):
        ans=[]
        odd=[]
        even=[]
        for i in range(len(A)):
            if A[i]%2==1:
                odd.append(A[i])
            else:
                even.append(A[i])

        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])

        return ans




print(Solution().sortArrayByParityII([4,2,5,7]))