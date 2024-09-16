class Solution(object):
    def average(self, salary):
        salary.sort()
        ans=0
        len(salary)
        for i in salary[1:len(salary)-1]:
            ans+=float(i)

        return ans/ (len(salary)-2)

print(Solution().average(salary = [4000,3000,1000,2000]))
print(Solution().average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))
