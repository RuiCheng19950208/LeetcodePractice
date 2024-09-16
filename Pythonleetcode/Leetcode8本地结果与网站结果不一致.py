class Solution(object):
    def myAtoi(self, str):
        input=''
        num=['1','2','3','4','5','6','7','8','9','0','+','-']
        for i in range(len(str)):
            if str[i]!=' ':
                input=input+str[i]
            elif  str[i-1] in num and str[i+1]in num:
                return 0


        output = 0
        mark=0
        value=0

        while (input != ''):
            if input[0] == '0':

                    input = input[1:]
            elif input[0] == '1':
                output = output + 1 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '2':
                output = output + 2 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '3':
                output = output + 3 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '4':
                output = output + 4 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '5':
                output = output + 5 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '6':
                output = output + 6 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '7':
                output = output + 7 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '8':
                output = output + 8 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0] == '9':
                output = output + 9 * (10 ** (len(input) - 1))
                input = input[1:]
            elif input[0]=='-':
                input = input[1:]
                mark=1
                value = value + 1
            elif input[0] == '+':
                input = input[1:]
                value=value+1


            else:
                output=output/(10**(len(input)))
                break
        if value>1:
            return 0
        if mark==1:
            output=-output
        if output<-2147483648:
            output=-2147483648
        if output>2147483647:
            output=2147483647

        return int(output)





print(Solution().myAtoi(" 4193 with words"))
print(Solution().myAtoi("-91283472332"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("42"))
print(Solution().myAtoi(" -42"))



print(Solution().myAtoi("0000123"))
print(Solution().myAtoi("-0000123"))
print(Solution().myAtoi("+0000123"))

print(Solution().myAtoi("+0 123"))

print(Solution().myAtoi("- 234"))