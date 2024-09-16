class Solution(object):
    def getNoZeroIntegers(self, n):
        str_n=str(n)
        ans_num_str=''
        if(len(str_n)==1):
            return[n-1,1]
        for i in range(1,len(str_n)):
            if(str_n[i]=="9"):
                ans_num_str = ans_num_str + "1"
            else:
                ans_num_str = ans_num_str + str(int(str_n[i]) + 1)


        return [int(ans_num_str),n-int(ans_num_str)]

print(Solution().getNoZeroIntegers(2))
print(Solution().getNoZeroIntegers(11))
print(Solution().getNoZeroIntegers(10000))
print(Solution().getNoZeroIntegers(69))
print(Solution().getNoZeroIntegers(1010))