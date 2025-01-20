public class Solution198 {
    public int Rob(int[] nums) {
        List<int> dp = new List<int>();
        for(int i=0;i<nums.Length+2;i++){dp.Add(0);}
        Console.WriteLine(dp.Count);
        for(int i=2;i<dp.Count;i++)
        {
            dp[i]=Math.Max(dp[i-1],dp[i-2]+nums[i-2]);
        }
        return dp[dp.Count-1];
    }
}