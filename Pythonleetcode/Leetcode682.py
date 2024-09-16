class Solution(object):
    def calPoints(self, ops):
        result=0
        for i in range(len(ops)):
            if ops[i]!='C' and ops[i]!='D' and ops[i]!='+':
                result=result+int(ops[i])
                ops[i]=int(ops[i])

            if ops[i]=='C':
                for j in range(i+1):
                    if ops[i-j]!=0 and ops[i-j]!='C':
                        result=result-ops[i-j]
                        ops[i]=0
                        ops[i-j]=0
                        break

            if ops[i] == 'D':
                for j in range(i+1):
                    if ops[i-j]!=0 and ops[i-j]!='D':
                        ops[i]=2*ops[i-j]
                        result = result + ops[i]
                        break

            if ops[i] == '+':
                count=2
                for j in range(i+1):
                    if ops[i-j]!=0 and ops[i-j]!='+' and count==2:
                        ops[i]=ops[i-j]
                        count=1
                        continue
                    if ops[i-j]!=0 and ops[i-j]!='+' and count==1:
                        ops[i] = ops[i]+ops[i - j]
                        count = 0
                        break
                result=result+ops[i]


        return result




print(Solution().calPoints( ["-60","D","-36","30","13","C","C","-33","53","79"]))
