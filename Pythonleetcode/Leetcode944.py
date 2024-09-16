class Solution(object):
    def minDeletionSize(self, A):
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        mat=[]
        for i in range(len(A[0])):
            s=[]
            for j in range(len(A)):
                s.append(alpha.index(A[j][i]))
            mat.append(s)
        ans=0
        for i in range(len(mat)):
            if sorted(mat[i])!=mat[i]:
                ans=ans+1


        return ans









print(Solution().minDeletionSize(["cba","daf","ghi"]))
print(Solution().minDeletionSize(["rrjk","furt","guzm"]))
