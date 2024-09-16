class Solution(object):
    def bitwiseComplement(self, N):
        def encode_into_binary_complement(N):
            str_n = bin(N)[2:]
            ans=''
            for i in  str_n:
                if(len(ans)>0 and i=="1" ):
                    ans =ans+'0'
                elif(i=='0'):
                    ans = ans + '1'
            if len(ans)==0:
                return "0"
            return ans
        def decode_into_binary(str_n):
            ans=0
            power_two_index=len(str_n)
            for i in str_n:
                power_two_index -=1
                if (i=="1"):
                    ans +=2**power_two_index

            return ans

        return decode_into_binary(encode_into_binary_complement(N))

print(Solution().bitwiseComplement(5))
print(Solution().bitwiseComplement(7))
print(Solution().bitwiseComplement(10))