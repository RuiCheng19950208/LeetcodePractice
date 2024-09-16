# class Solution(object):
#     def findAnagrams(self, s, p):
#         a=len(s)
#         b=len(p)
#         c=sorted(p)
#         ans=[]
#         for i in range(a-b+1):
#             if sorted(s[i:i+b])==sorted(p):
#                 ans.append(i)
#         return ans
#chaoshi


class Solution(object):
    def findAnagrams(self, s, p):
        if len(s)<len(p):
            return []
        tongjis=[0]*130
        tongjip=[0]*130
        a,b=len(s),len(p)
        for i in range(b):
            tongjip[ord(p[i])]=tongjip[ord(p[i])]+1
            tongjis[ord(s[i])] = tongjis[ord(s[i])] + 1
        ans=[]
        for i in range(b,a):
            if tongjip==tongjis:
                ans.append(i-b)
            if i==a-1:
                break
            tongjis[ord(s[i])]=tongjis[ord(s[i])]+1
            tongjis[ord(s[i-b])] = tongjis[ord(s[i-b])] - 1

        tongjis[ord(s[a-1])] = tongjis[ord(s[a-1])] + 1
        tongjis[ord(s[a - b-1])] = tongjis[ord(s[a - b-1])] - 1
        if tongjip == tongjis:
            ans.append(a - b)


        return ans











print(Solution().findAnagrams("cbaebabacd" ,"abc"))
print(Solution().findAnagrams("abab","ab"))