class Solution(object):
    def merge(self, intervals):
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        ans=[]
        start_index=0
        while(start_index<len(intervals)):
            end_index = start_index+1
            prev_index = end_index-1
            temp_small = intervals[start_index][0]
            temp_big = intervals[start_index][1]
            # print(start_index, end_index, prev_index)
            while end_index<len(intervals) and intervals[end_index][0]<=temp_big:
                temp_big = max(intervals[end_index][1],temp_big)
                temp_small = min(intervals[end_index][0], temp_small)
                end_index+=1
                prev_index+=1
            ans.append([temp_small,temp_big])
            start_index=end_index
            if start_index>=len(intervals):
                break
        return ans


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge( [[1,4],[4,5]]))
print(Solution().merge( [[1,4],[0,4]]))
print(Solution().merge( [[1,4],[0,0]]))