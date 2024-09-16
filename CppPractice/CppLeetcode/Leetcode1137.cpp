#include<vector>
using namespace std;

class Solution {
public:
    int tribonacci(int n) 
    {
        vector<int> dp={0,1,1};

        if (n<3)
        {
            return dp[n];
        }
        int cur=3;
        while (cur<=n)
        {
            dp.push_back(dp[cur-1]+dp[cur-2]+dp[cur-3]);
            cur++;
        }
        return dp.back();
    }
};