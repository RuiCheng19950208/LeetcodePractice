class Solution(object):
    def letterCasePermutation(self, S):
        res=[]
        res.append(S)

        def add(res,j):
            for i in res:
                if i[:j]+i[j].upper()+i[j+1:] not in res:
                     res.append(i[:j]+i[j].upper()+i[j+1:])
                if i[:j]+i[j].lower()+i[j+1:] not in res:
                     res.append(i[:j]+i[j].lower()+i[j+1:])


        for j in range(0,len(S)):
            add(res,j)
        return res







print(Solution().letterCasePermutation("a1b2"))