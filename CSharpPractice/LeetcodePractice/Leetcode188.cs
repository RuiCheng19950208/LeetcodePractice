public class Solution188 {
    public int MaxProfit(int k, int[] prices) 
    {
        List<int> sells = new List<int>();
        List<int> buys = new List<int>();
        for(int i=0;i<k;i++)
        {
            sells.Add(0);
            buys.Add(-10000000);
        }
        for(int i=0;i<prices.Length;i++)
        {
            for(int j=0;j<k;j++)
            {
                if(j==0){buys[j]=Math.Max(buys[j],-prices[i]);}
                else{buys[j]=Math.Max(buys[j],sells[j-1]-prices[i]);}
                sells[j]=Math.Max(sells[j],buys[j]+prices[i]);
            }
        }
        return sells[k-1];
    }
}