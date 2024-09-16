class Solution(object):
    def numSpecialEquivGroups(self, A):
        if len(A[0])==0:
            return 1
        result=1
        odd = []
        even=[]
        zuhe=[]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if j%2==1:
                    even.append(A[i][j])
                else:
                    odd.append(A[i][j])
                even.sort()
                odd.sort()
            if [even,odd] not in zuhe:
                    zuhe.append([even,odd])
                    if i!=0:
                        result = result + 1

            else:
                    odd = []
                    even = []
                    continue

            odd=[]
            even=[]

        return result




print(Solution().numSpecialEquivGroups(["a","b","c","a","c","c"]))
print(Solution().numSpecialEquivGroups(["aa","bb","ab","ba"]))
print(Solution().numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))
print(Solution().numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))
