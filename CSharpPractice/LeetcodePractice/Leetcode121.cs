public class Solution121 {
    public int MaxProfit(int[] prices) 
    {
        int ans = 0;
        int minPrice = int.MaxValue;
        int curPrice = 0;
        int temp=0;
        foreach(int price in prices)
        {
            minPrice = Math.Min(price,minPrice);
            temp = price - minPrice;
            ans = Math.Max(temp,ans);
        }
        return ans;
    }
}