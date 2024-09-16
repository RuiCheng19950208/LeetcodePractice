
class Solution(object):
    def findWords(self, words):

        C=[]
        for i in words:
            C.append(i.upper())

        Q={'Q','W','E','R','T','Y','U','I','O','P'}
        A={'A','S','D','F','G','H','J','K','L'}
        Z={'Z','X','C','V','B','N','M'}
        ans=[]
        for i in range(len(C)):
            if set(C[i]).intersection(set(Q))==set(C[i]) or set(C[i]).intersection(set(A))==set(C[i]) or set(C[i]).intersection(set(Z))==set(C[i]):
                ans.append(words[i])
        return ans








print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))