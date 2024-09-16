#include<vector>
class Solution {
private:
    int sumVector(vector<int> theVector)
    {
        int ans=0;
        for (int i = 0; i < theVector.size(); i++)
        {
            ans += theVector[i];
        }
        return ans;
    }
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) 
    {
        int total = (n+rolls.size()) * mean;
        int totalRemain = total - sumVector(rolls);
        if (totalRemain < n || totalRemain>6*n)
        {
            return vector<int>();
        }
        int remainder = totalRemain - n;
        vector<int> ans(n,1);
        int index = 0;
        while (remainder>0)
        {
            int support = 6-ans[index]>remainder?remainder:6-ans[index];
            ans[index] += support;
            remainder -= support;
            index++;
        }
        return ans;
    }
};