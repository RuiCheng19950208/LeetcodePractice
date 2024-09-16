class Solution(object):
    def readBinaryWatch(self, num):
        res = []
        for hour in range(12):
            for minute in range(60):
                if (bin(hour) + bin(minute)).count('1') == num:
                    res.append("%d:%02d" % (hour, minute))
        return res

print(Solution().readBinaryWatch(1))