public class Solution123 {
    public int MaxProfit(int[] prices) 
    {
        List<int> buys = new List<int>{-1000000,-1000000};
        List<int> sells = new List<int>{0,0};
        int n=sells.Count;
        for(int i=0;i<prices.Length;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(j==0){buys[j]=Math.Max(buys[j],-prices[i]);}
                else{buys[j]=Math.Max(buys[j],sells[j-1]-prices[i]);}
                sells[j]=Math.Max(sells[j],buys[j]+prices[i]);
            }
        }
        return sells[n-1];
    }
}