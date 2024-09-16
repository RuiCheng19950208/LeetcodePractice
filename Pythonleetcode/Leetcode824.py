class Solution(object):
    def toGoatLatin(self, S):
        S=S.split(' ')
        for i in range(0,len(S)):

            if S[i][0]=='a' or S[i][0]=='A' or S[i][0]=='e' or S[i][0]=='E' or S[i][0]=='I' or S[i][0]=='i'or S[i][0]=='O' or S[i][0]=='o' or S[i][0]=='U' or S[i][0]=='u':

                S[i]=S[i]+'ma'
            else:
                S[i]=S[i][1:]+S[i][0]+'ma'

        for i in range(0,len(S)):
            for j in range(0, i+1):
                S[i]=S[i]+'a'

        ans=S[0]
        for i in range(1,len(S)):
            ans=ans+' '+S[i]

        return ans








print(Solution().toGoatLatin("I speak Goat Latin"))