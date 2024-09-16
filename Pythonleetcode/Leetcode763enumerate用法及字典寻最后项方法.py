class Solution(object):
    def partitionLabels(self, S):
        last={c:i for i,c in enumerate(S)}
        ans=[]
        j=anchor=0
        for i,c in enumerate(S):
            j=max(j,last[c])
            if i==j:
                ans.append(i-anchor+1)
                anchor=i+1

        return ans







print(Solution().partitionLabels("ababcbacadefegdehijhklij"))