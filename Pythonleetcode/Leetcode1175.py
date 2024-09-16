class Solution(object):
    def numPrimeArrangements(self, n):
        if n==1:
            return 1

        def fract(n):
            ans=1
            for i in range(1,n+1):
                ans=ans*i
            return ans
        is_prime=[True]*(n+1)
        is_prime[0],is_prime[1]=False,False
        for i in range(2,n+1):
            for j in range(i):
                if(is_prime[j]==True and i%j==0):
                    is_prime[i]=False
                    break
        prime_number=len([i for i in is_prime if i==True])
        nonprime_number = len([i for i in is_prime if i==False])-1
        modulo=10**9+7

        return (fract(prime_number)*fract(nonprime_number))%modulo

print(Solution().numPrimeArrangements(5))
print(Solution().numPrimeArrangements(100))