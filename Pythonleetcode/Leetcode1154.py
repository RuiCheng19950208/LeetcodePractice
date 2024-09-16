class Solution(object):
    def dayOfYear(self, date):
        day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
        time_list=date.split("-")
        year=int(time_list[0])
        month=int(time_list[1])
        day=int(time_list[2])
        if((year%4==0 and year%100!=0 ) or((year%400==0 and year%100==0 )) ):
            day_list[1] +=1
        else:
            pass
        ans=0
        if(month==1):
            ans=day
        else:
            for i in range(month-1):
                ans+=day_list[i]
            ans +=day

        return ans


print(Solution().dayOfYear("2019-01-09"))
print(Solution().dayOfYear("2019-02-10"))
print(Solution().dayOfYear("2003-03-01"))
print(Solution().dayOfYear("2000-03-01"))