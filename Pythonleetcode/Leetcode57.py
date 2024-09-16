class Solution(object):
    def insert(self, intervals, newInterval):
        ans=[]
        if len(intervals)==0:
            return [newInterval]
        start_index=0
        end_index=0
        temp_min = newInterval[0]
        temp_max = newInterval[1]
        while start_index<len(intervals):
            if intervals[start_index][1]>=newInterval[0] and intervals[start_index][0]<=newInterval[1]:
                temp_min = min(intervals[start_index][0],newInterval[0])
                temp_max = max(intervals[start_index][1],newInterval[1])
                break
            start_index += 1
        end_index = start_index+1
        while end_index<len(intervals):
            if intervals[end_index][0]<=temp_max:
                temp_min = min(intervals[end_index][0],temp_min)
                temp_max = max(intervals[end_index][1], temp_max)
                end_index+=1
            else:
                break


        # print(start_index,end_index)
        for i in range(len(intervals)):
            if i<start_index:
                ans.append(intervals[i])
            if i>=end_index:
                ans.append(intervals[i])
        ans.append([temp_min,temp_max])
        ans.sort(key=lambda x:x[0])
        return ans

print(Solution().insert( intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(Solution().insert( intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(Solution().insert( intervals = [], newInterval = [5,7]))
print(Solution().insert( intervals = [[1,5]], newInterval = [2,3]))
