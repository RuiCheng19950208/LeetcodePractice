class Solution(object):
    def countAndSay(self, n):
        def str2num(input):
            output=0
            while (input!=''):
                if input[0]=='0':
                    input = input[1:]
                elif input[0]=='1':
                    output=output+1*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='2':
                    output=output+2*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='3':
                    output=output+3*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='4':
                    output=output+4*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='5':
                    output=output+5*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='6':
                    output=output+6*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='7':
                    output=output+7*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='8':
                    output=output+8*(10**(len(input)-1))
                    input=input[1:]
                elif input[0]=='9':
                    output=output+9*(10**(len(input)-1))
                    input=input[1:]
            return output


        def cs(input):
            output=''
            if input=='':
                return '1'
            elif input=='1':
                return '11'
            else:
                numset=[input[0]]
                countset=[]
                count=1
                startpoint=1
                while startpoint!=len(input):
                    if input[startpoint]==input[startpoint-1]:
                        count=count+1
                    else:
                        countset.append(str(count))
                        count=1
                        numset.append(input[startpoint])
                    startpoint=startpoint+1
                if len(numset)!=len(countset):
                    countset.append(str(count))
                n=0
                while(n!=len(numset)):
                    output=output+countset[n]+numset[n]
                    n=n+1
                return output




        c=0
        input=''
        while (c<n):
            input = cs(input)
            c=c+1
        return str(str2num(input))





print(Solution().countAndSay(1))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))
print(Solution().countAndSay(6))