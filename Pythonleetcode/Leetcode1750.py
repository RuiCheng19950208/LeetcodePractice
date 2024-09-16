class Solution(object):
    def minimumLength(self, s):
        ans=len(s)
        left=0
        right=len(s)-1
        if len(s)==1:
            return 1
        if len(set(s))==1:
            return 0
        while True:
            if s[left]!=s[right]:
                break
            else:
                while s[left+1]==s[left]:
                    left+=1
                    ans-=1
                left+=1
                ans-=1
                if left>right:
                    return 0
                else:
                    while s[right -1 ] == s[right]:
                        right -= 1
                        ans-=1
                right -= 1
                ans-=1
            if right==left:
                return 1
            # print(right,left,ans)
        return ans

print(Solution().minimumLength( s = "ca"))
print(Solution().minimumLength( s = "cabaabac"))
print(Solution().minimumLength( s = "aabccabba"))