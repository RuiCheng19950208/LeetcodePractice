class Solution(object):
    def reformatDate(self, date):
        date_list=date.split(" ")
        month_dict={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        day_str = date_list[0][:-2]
        if len(day_str)==1:
            day_str="0"+day_str
        month_str=month_dict[date_list[1]]
        year_str=date_list[2]
        ans=year_str+"-"+month_str+"-"+day_str
        return ans

print(Solution().reformatDate(date = "20th Oct 2052"))
print(Solution().reformatDate(date = "6th Jun 1933"))
print(Solution().reformatDate(date = "26th May 1960"))