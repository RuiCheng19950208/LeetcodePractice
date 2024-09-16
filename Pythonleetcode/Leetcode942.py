class Solution(object):
    def diStringMatch(self, S):
        if S=='':
            return [0]
        result = []
        ele = []
        if S[0]=='I':
            result.append(0)
            for i in range(len(S)):
                ele.append(i + 1)
        else:
            result.append(len(S))
            for i in range(len(S)):
                ele.append(i)

        for i in range(len(S)-1):
            if S[i]=="I":
                if S[i+1]=='I':
                    result.append(ele[0])
                    ele.pop(0)

                else:
                    result.append(ele[-1])
                    ele.pop(-1)
            if S[i] == "D":
                if S[i+1]=='D':
                    result.append(ele[-1])
                    ele.pop(-1)
                else:
                    result.append(ele[0])
                    ele.pop(0)
        result.append(ele[0])
        return result




print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("DIDI"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDDIII"))