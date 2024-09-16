class Solution(object):
    def countVowelStrings(self, n):

        end_symbpol=[1,1,1,1,1]
        if n==1:
            return 5
        else:
            for i in range(n-1):
                for j in range(len(end_symbpol)):
                    for k in range(j):
                        end_symbpol[k] += end_symbpol[j]
            return sum(end_symbpol)




print(Solution().countVowelStrings(1))
print(Solution().countVowelStrings(2))
print(Solution().countVowelStrings(33))