# class Solution(object):
#     def countPrimeSetBits(self, L, R):
#
#
#         def prime(n):
#             i = 0
#             ans = 0
#             count=0
#             while (n != 0):
#                 yushu = n % 2
#                 n = n // 2
#                 if yushu==1:
#                     count=count+1
#
#             if count in [2,3,5,7,11,13,17,19]:
#                 return True
#             else:
#                 return False
#         ans=0
#         for i in range(L,R+1):
#             if prime(i):
#                 ans=ans+1
#
#         return ans
#       超时



# class Solution(object):
#     def countPrimeSetBits(self, L, R):
#         primes = {2, 3, 5, 7, 11, 13, 17, 19}
#         return sum(bin(x).count('1') in primes
#                    for x in range(L, R+1))
#标准答案




class Solution(object):
    def countPrimeSetBits(self, L, R):
        count=0
        prime=[2,3,5,7,11,13,17,19]
        for i in range(L,R+1):
            if bin(i).count('1') in prime:
                count=count+1
        return count






print(Solution().countPrimeSetBits(6,10))
print(Solution().countPrimeSetBits(10,15))