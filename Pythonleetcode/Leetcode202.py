class Solution(object):
    def isHappy(self, n):

        def back(n):
            m=0
            while n!=0:
                m=m+(n%10)**2
                n=n//10
            return m

        his=[n]
        while True:
            if n==1:
                return True

            n=back(n)



            if n in his:
                return False
            elif n==1:
                return True
            his.append(n)


print(Solution().isHappy(19))