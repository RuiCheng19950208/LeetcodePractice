class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        th=[0]*len(primes)
        a=1
        ans=[1]
        while a!=n:
            a = a + 1
            b = []

            for i in range(len(primes)):
                b.append(ans[th[i]]*primes[i])

            mi=min(b)
            ans.append(mi)
            for i in range(len(primes)):
                if ans[-1]==ans[th[i]]*primes[i]:
                    th[i]=th[i]+1



        return ans[-1]

print(Solution().nthSuperUglyNumber(12,[2,7,13,19]))