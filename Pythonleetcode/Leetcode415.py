class Solution(object):
    def addStrings(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        number1=0
        number2 = 0
        for i in range(len(num1)):
            if num1[i]=='1':
                number1=number1+(10**i)*1
            if num1[i]=='2':
                number1=number1+(10**i)*2
            if num1[i]=='3':
                number1=number1+(10**i)*3
            if num1[i]=='4':
                number1=number1+(10**i)*4
            if num1[i]=='5':
                number1=number1+(10**i)*5
            if num1[i]=='6':
                number1=number1+(10**i)*6
            if num1[i]=='7':
                number1=number1+(10**i)*7
            if num1[i]=='8':
                number1=number1+(10**i)*8
            if num1[i]=='9':
                number1=number1+(10**i)*9



        for i in range(len(num2)):
            if num2[i]=='1':
                number2=number2+(10**i)*1
            if num2[i]=='2':
                number2=number2+(10**i)*2
            if num2[i]=='3':
                number2=number2+(10**i)*3
            if num2[i]=='4':
                number2=number2+(10**i)*4
            if num2[i]=='5':
                number2=number2+(10**i)*5
            if num2[i]=='6':
                number2=number2+(10**i)*6
            if num2[i]=='7':
                number2=number2+(10**i)*7
            if num2[i]=='8':
                number2=number2+(10**i)*8
            if num2[i]=='9':
                number2=number2+(10**i)*9
        result=number1+number2
        return str(result)





print(Solution().addStrings('11','109'))
