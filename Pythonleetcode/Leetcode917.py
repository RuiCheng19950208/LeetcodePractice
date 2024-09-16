class Solution(object):
    def reverseOnlyLetters(self, S):
        chara=[]
        nonchara=[]

        inde=[]

        for i in range(len(S)):
            if S[i].isalpha():
                chara.append(S[i])
            else:
                nonchara.append(S[i])
                inde.append(i)

        ans = []
        chara=chara[::-1]
        i=0

        while(chara!=[] or nonchara!=[]):
            if i in inde:
                ans.append(nonchara[0])
                nonchara.pop(0)
                i=i+1
            else:
                ans.append(chara[0])
                chara.pop(0)
                i=i+1

        result=''
        for i in range(len(ans)):
            result=result+str(ans[i])

        return result



print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))