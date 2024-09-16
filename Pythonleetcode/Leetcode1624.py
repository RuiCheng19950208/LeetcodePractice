class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        ans=-1
        starting_index=0
        end_index=len(s)-1
        while True:
            # print(starting_index,end_index)
            if s[starting_index]==s[end_index] and end_index-starting_index-1>ans:
                ans=end_index-starting_index-1
                if ans > len(s) - starting_index - 2:
                    return ans
            end_index-=1
            if end_index==starting_index:
                starting_index+=1
                end_index=len(s)-1
            if starting_index>=len(s)-2:
                break


        return ans


print(Solution().maxLengthBetweenEqualCharacters(s = "aa"))
print(Solution().maxLengthBetweenEqualCharacters( s = "abca"))
print(Solution().maxLengthBetweenEqualCharacters( s = "cbzxy"))
print(Solution().maxLengthBetweenEqualCharacters(s = "cabbac"))
