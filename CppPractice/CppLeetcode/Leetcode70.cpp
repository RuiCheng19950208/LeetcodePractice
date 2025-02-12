class Solution {
public:
    int climbStairs(int n) 
    {
        vector<int>dp(n+1,0);
        if(n<=1){return 1;}
        dp[0]=1;
        dp[1]=1;
        for(int i=2;i<dp.size();i++)
        {
            dp[i] = dp[i-1]+dp[i-2];
        }
        return dp[dp.size()-1];
        
    }
};