class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g=sorted(g)
        s=sorted(s)
        child_index=len(g)-1
        cookie_index=len(s)-1
        ans=0
        if len(s)==0:
            return 0
        while child_index>-1 and cookie_index>-1:
            if s[cookie_index]>=g[child_index]:
                ans +=1
                child_index -=1
                cookie_index -=1

            else:
                child_index -=1

        return ans




print(Solution().findContentChildren( [1,2,3], [1,1]))
print(Solution().findContentChildren( [1,2], [1,2,3]))
print(Solution().findContentChildren( [10,9,8,7],[5,6,7,8]))

