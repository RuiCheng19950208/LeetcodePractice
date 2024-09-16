class Solution(object):
    def buddyStrings(self, A, B):
        if len(A)!=len(B):
            return False

        E=[]
        F=[]
        for i in range(len(A)):
            E.append(A[i])
            F.append(B[i])
        E.sort()
        F.sort()
        if E!=F:
            return False
        if len(set(A))!=len(A):
            error = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    error = error + 1
            if error==0 or error==2:
                return True
            else:
                return False
        else:
            error=0
            for i in range(len(A)):
                if A[i]!=B[i]:
                    error=error+1
            if error==2:
                return True
            else:
                return  False




print(Solution().buddyStrings("aaaaaaabc","aaaaaaacb"))