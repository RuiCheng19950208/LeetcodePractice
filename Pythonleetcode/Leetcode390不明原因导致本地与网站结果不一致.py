class Solution(object):
    def lastRemaining(self, n):
        plusdivide=0
        divide=0
        string=[]
        for i in range(1,n+1):
            string.append(i)
        while(len(string)>1):
            if divide <= plusdivide:
                for i in range(len(string)):
                    if string[i] % 2 == 1:
                        string[i]=0

                string = [i/2 for i in string if i!=0]


                divide=divide+1
            else:
                string = [i + 1 for i in string]
                if string[-1]%2==1:
                    for i in range(len(string)):
                        if string[i] % 2 == 1:
                            string[i] = 0
                else:
                    for i in range(len(string)):
                        if string[i] % 2 == 0:
                            string[i] = 0

                string = [i / 2 for i in string if i!=0]


                plusdivide = plusdivide + 1


        ans=string[0]
        while(plusdivide!=0 or divide!=0):
            if divide>plusdivide:
                ans=ans*2
                divide=divide-1


            else:
                ans = (ans * 2)-1
                plusdivide = plusdivide - 1


        return int(ans)






print(Solution().lastRemaining(6))
print(Solution().lastRemaining(9))

