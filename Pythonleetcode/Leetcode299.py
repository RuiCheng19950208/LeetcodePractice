class Solution(object):
    def getHint(self, secret, guess):
        A=0
        B=0
        sd = {}
        gd = {}
        for i in secret+guess:
            sd[i]=0
            gd[i] = 0

        for i in range(len(secret)):
            if secret[i]==guess[i]:
                A=A+1
            else:
                sd[secret[i]]=sd[secret[i]]+1
                gd[guess[i]] = gd[guess[i]] + 1
        # print(sd,gd)
        for i in gd:
            B=B+min(gd[i],sd[i])
        return '%dA%dB'%(A,B)





print(Solution().getHint("1123","0111"))