import copy
class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans=[]

        def zichu(n):
            m=copy.deepcopy(n)
            while n!=0:
                yu=n%10
                if yu==0:
                    return 0
                if m%yu!=0:
                    return 0
                n=int((n-yu)/10)




            return m



        for i in range(left,right+1):
            ans.append(zichu(i))

        bns=[]
        for i in ans:
            if i!=0:
                bns.append(i)


        return bns




print(Solution().selfDividingNumbers(1,22))