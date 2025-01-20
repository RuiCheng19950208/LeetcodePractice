class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(amount==0){return 0 ;}
        // sort(coins.begin(),coins.end());
        vector<int> dp(amount+1,-1);
        dp[0]=0;
        for(int i=1;i<dp.size();i++)
        {
            for(int coin:coins)
            {
                if(coin<=i && dp[i-coin]!=-1)
                {
                    if(dp[i]==-1){dp[i]=dp[i-coin]+1;}
                    else{dp[i] = min(dp[i-coin]+1,dp[i]);}
                }
            }
        }
        return dp[dp.size()-1];
    }
};