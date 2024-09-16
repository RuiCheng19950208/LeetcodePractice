class Solution(object):
    def shortestToChar(self, S, C):
        result=[]
        def ans(S,C,i):
            if S[i]==C:
                return 0
            l=1000
            r=999

            for j in range(1000):
                if S[i+j]==C :
                    r=j
                    break
                if i+j+1==len(S):
                    break
            for k in range(1000):
                if S[i-k]==C:
                    l=k
                    break
                if i-k==0:
                    break

            return min([l,r])

        for i in range(len(S)):
            result.append(ans(S,C,i))

        return result



print(Solution().shortestToChar("loveleetcode",'e'))
print(Solution().shortestToChar("baaa",'b'))