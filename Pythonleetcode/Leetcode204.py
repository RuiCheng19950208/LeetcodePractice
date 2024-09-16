# class Solution(object):
#     def countPrimes(self, n):
#         m=1
#         if n==0 or n==1 or n==2:
#             return 0
#
#         for i in range(3,n):
#             if i%2==0:
#                 continue
#             m=m+1
#             for j in range(2,int(i**0.5)+1):
#                 if (i%j==0):
#                     m = m -1
#                     break
#
#                 else:
#                     continue
#
#         return m


class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n

        primes[0] = primes[1] = False
        print(primes)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
                print(len(primes[i * i: n: i]))
                print(primes)
        return sum(primes)


print(Solution().countPrimes(10))