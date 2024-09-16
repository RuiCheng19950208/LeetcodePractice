class Solution(object):
    def uncommonFromSentences(self, A, B):
        C=A.split(' ')
        D = B.split(' ')
        E=C+D
        E.sort()
        Ans=[]

        for i in E:
            if E.count(i)==1:
                Ans.append(i)
        return Ans


print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))