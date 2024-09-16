#include<vector>
using namespace std;

class Solution338 {
public:
    vector<int> countBits(int n) {

        vector<int> dp(n+1,0);
        if(n==0)
        {
            return dp;
        }
        dp[1] = 1;
        for(int i = 0; i < dp.size(); i++)
        {
            if(i%2==0)
            {
                dp[i]=dp[i/2];
            }
            else
            {
                dp[i] = dp[i/2]+1;
            }
        }
        return dp;
        
    }
};