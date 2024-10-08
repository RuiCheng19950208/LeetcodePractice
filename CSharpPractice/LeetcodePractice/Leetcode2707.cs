public class Solution2707 {
    public int MinExtraChar(string s, string[] dictionary) {
        int[] dp =  new int[s.Length+1];
        for (int i = 0; i < dp.Length; i++)
        {
            dp[i]=i;
        }
        for (int i = 1; i < dp.Length; i++)
        {
            dp[i] = dp[i-1]+1;
            foreach (var key in dictionary)
            {
                int lenk = key.Length;
                if (lenk<=i)
                {
                    if (s.Substring(i-lenk,lenk)==key)
                    {
                        // Console.WriteLine(s.Substring(i-lenk,lenk));
                        dp[i] = Math.Min(dp[i],dp[i-lenk]);
                        
                    }
                }
            }
        }
        return dp[dp.Length-1];
    }
}