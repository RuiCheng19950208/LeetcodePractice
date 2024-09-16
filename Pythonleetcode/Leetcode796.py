class Solution(object):
    def rotateString(self, A, B):
        if len(A)!=len(B):
            return False
        l=len(A)
        if len(A)==0:
            return True
        if len(A)==1:
            if A==B:
                return True
            else:return False
        for i in range(l):
            A=A[1:]+A[0]
            if A==B:
                return True
        return False



print(Solution().rotateString('abcde', 'cdeab'))