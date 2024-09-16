class Solution:

    def generateParenthesis(self, n):

        ans=[]

        def back(s='',left=0 ,right=0):
            if len(s)==2*n:
                ans.append(s)
            if left<n:
                back(s+'(',left+1,right)

            if left>right:
                back(s+')',left,right+1)
        back()


        return ans



print(Solution().generateParenthesis(3))
