var coinChange = function(coins, amount) {
    if(amount==0){return 0;}
    let dp = Array(amount+1).fill(-1);
    dp[0]=0;
    for(let i=1;i<dp.length;i++)
    {
        for(let coin of coins)
        {
            if(coin<=i && dp[i-coin]!=-1)
            {
                if(dp[i]==-1){dp[i]=dp[i-coin]+1;}
                else{dp[i] = Math.min(dp[i-coin]+1,dp[i]);}
            }

        }
    }
    return dp[dp.length-1];
};