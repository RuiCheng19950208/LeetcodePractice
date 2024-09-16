class Solution(object):
    def complexNumberMultiply(self, a, b):

        def str2num(input):
            output = 0
            mark=0
            while (input != ''):

                if input[0] == '-':
                    input = input[1:]
                    mark=1

                elif input[0] == '0':
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

            if mark==0:
                return output
            else:
                return -output

        def str2imnum(s):
            a=''
            b=''
            mark=0
            for i in s:
                if i!='+' and mark==0:
                    a=a+i
                else: mark=1

                if mark==0:
                    continue
                elif i!='i'and i!='+' and mark==1:
                    b=b+i


            return str2num(a),str2num(b)

        a1=str2imnum(a)[0]
        a2=str2imnum(a)[1]
        b1 = str2imnum(b)[0]
        b2 = str2imnum(b)[1]

        real=a1*b1-a2*b2

        image=a1*b2+a2*b1

        return str(real)+'+'+str(image)+'i'
















print(Solution().complexNumberMultiply("1+1i", "1+1i"))
print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))