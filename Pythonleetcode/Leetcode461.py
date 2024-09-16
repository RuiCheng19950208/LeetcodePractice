class Solution(object):
    def hammingDistance(self, x, y):
        def erjin(n):
            k = ''

            while n!=0:

                k=k+str(n%2)
                n = n // 2


            return k

        w = erjin(x)
        z = erjin(y)



        if len(w)>len(z):
            long=w
            short=z

        else:
            long = z
            short = w

        k=0
        for i in range(len(short),len(long)):
            if long[i]=='1':
                k=k+1

        for i in range(0, len(short)):
            if long[i]!=short[i]:
                k=k+1


        return k





print(Solution().hammingDistance(10,4))