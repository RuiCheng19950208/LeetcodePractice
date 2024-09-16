class Solution(object):
    def characterReplacement(self, s, k):
        count_list=[0]*26
        r=0
        l=0
        ans=0
        while r<len(s):
            count_list[ord(s[r])-ord("A")]+=1
            r+=1
            if r-l-max(count_list)>k:
                count_list[ord(s[l])-ord("A")]-=1
                l+=1
            ans=max(ans,sum(count_list))
            # print(l,r,ans,max(count_list))

        return ans

print(Solution().characterReplacement(s = "ABAB", k = 2))
print(Solution().characterReplacement(s = "AABABBA", k = 1))