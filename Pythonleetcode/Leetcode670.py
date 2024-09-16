class Solution(object):
    def maximumSwap(self, num):
        def encode_list(n):
            ans=[]
            while n!=0:
                ans.append(n%10)
                n=n//10
            return ans[::-1]

        def decode_list(lis):
            ans=0
            for i, x in enumerate(lis[::-1]):
                ans+=x*10**i
            return ans

        num_list=encode_list(num)[::-1]

        for i,x in enumerate(num_list):
            max_num = max(num_list[:len(num_list)-i])
            # print(num_list[:len(num_list)-i])
            if(num_list[len(num_list)-i-1]==max_num):
                continue
            else:
                target_list=num_list[:len(num_list)-i]
                for j,y in enumerate(target_list):
                    if y==max_num:
                        num_list[len(num_list)-i-1],num_list[j]= num_list[j],num_list[len(num_list)-i-1]
                        return decode_list(num_list[::-1])

        return decode_list(num_list[::-1])



print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(98368))