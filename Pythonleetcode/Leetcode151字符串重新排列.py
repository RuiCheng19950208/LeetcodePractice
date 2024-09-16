class Solution(object):
    def reverseWords(self, s):
        list1 = s.split()
        list1=list1[::-1]
        l=len(list1)

        ans=''
        for i in range(l):
            ans=ans+list1[i]
            if i!=l-1:
                ans=ans+' '

        return ans







print(Solution().reverseWords("the sky is blue"))