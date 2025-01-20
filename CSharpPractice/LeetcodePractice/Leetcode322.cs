public class Solution322 {
    public int CoinChange(int[] coins, int amount) 
    {
        List<int> dp = new List<int>();
        for(int i=0;i<amount+1;i++)
        {
            dp.Add(-1);
        }
        dp[0]=0;
        // Console.WriteLine(dp);
        for(int i=1;i<dp.Count;i++)
        {
            foreach(int coin in coins)
            {
                if(i>=coin && dp[i-coin]!=-1)
                {
                    if(dp[i]==-1){dp[i]=dp[i-coin]+1;}
                    else{dp[i]=Math.Min(dp[i],dp[i-coin]+1);}
                }
            }
        }
        return dp[dp.Count-1];
    }
}