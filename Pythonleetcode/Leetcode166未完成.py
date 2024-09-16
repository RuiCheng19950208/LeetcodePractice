class Solution(object): #(计算失败，无法计算1、17的情形)
    def fractionToDecimal(self, numerator, denominator):

        def generate_result(ans,decimal_list,repeat_index):
            for i in range(len(decimal_list)-1,-1,-1):
                if decimal_list[i]==0:
                    repeat_index-=1
                    decimal_list.pop()
                else:
                    break

            for i in range(len(decimal_list)):
                if i==repeat_index:
                    ans+="("+str(decimal_list[i])
                else:
                    ans+=str(decimal_list[i])
            ans+=")"
            return ans

        ans=""
        if(numerator>=0 and denominator<0) or (numerator<0 and denominator>=0):
            ans +="-"
        ans +=str(numerator//denominator)
        remainder=numerator%denominator
        if remainder!=0:
            ans+="."
        decimal_list=[]

        while True:
            next_decimal=(remainder*10)//denominator
            remainder=(remainder*10)%denominator
            if remainder==0:
                for i in range(len(decimal_list)):
                    ans+=str(decimal_list[i])
                if next_decimal!=0:
                    ans+=str(next_decimal)
                    return ans
                else:
                    return ans
            else:
                if next_decimal in decimal_list and next_decimal!=0:
                    for i in range(len(decimal_list)-1,-1,-1):
                        if decimal_list[i]==next_decimal:
                            repeat_index=i
                            return generate_result(ans,decimal_list,repeat_index)
                else:
                    decimal_list.append(next_decimal)








print(Solution().fractionToDecimal(numerator = 1, denominator = 2))
print(Solution().fractionToDecimal(numerator = 2, denominator = 1))
print(Solution().fractionToDecimal(numerator = 2, denominator = 3))
print(Solution().fractionToDecimal(numerator = 4, denominator = 333))
print(Solution().fractionToDecimal(numerator = 1, denominator = 333))