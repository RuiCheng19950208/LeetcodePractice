class Solution(object):
    def sortArrayByParity(self, A):
        Q=[]
        E=[]
        for i in A:
            if i%2==1:
                Q.append(i)
            else:
                E.append(i)
        return (E+Q)




print(Solution().sortArrayByParity([3,1,2,4]))