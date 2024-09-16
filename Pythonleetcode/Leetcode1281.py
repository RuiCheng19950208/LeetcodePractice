class Solution(object):
    def subtractProductAndSum(self, n):
        ans=0
        product=1
        summ=0
        while True:
            if n//10!=0:
                summ += n%10
                product *= n % 10
                n=n//10
            else:
                summ += n % 10
                product *= n % 10
                break
        ans=product-summ
        return ans






print(Solution().subtractProductAndSum(234))
print(Solution().subtractProductAndSum(4421))



