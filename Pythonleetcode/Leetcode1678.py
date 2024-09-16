class Solution(object):
    def interpret(self, command):
        str_index=0
        ans=""
        while str_index<len(command):
            if command[str_index]=='(':
                if command[str_index+1]=="a":
                    ans+="al"
                    str_index+=4
                else:
                    ans += "o"
                    str_index += 2
            elif command[str_index]=='G':
                ans += "G"
                str_index += 1

        return ans

print(Solution().interpret(command = "G()(al)"))
print(Solution().interpret(command = "G()()()()(al)"))
print(Solution().interpret(command = "(al)G(al)()()G"))
