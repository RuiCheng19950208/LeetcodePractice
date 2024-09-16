using System.Runtime.InteropServices;

public class Solution44 {
    public bool IsMatch(string s, string p) 
    {
        int sLen = s.Length;
        int pLen = p.Length;
        bool[,] dp = new bool[sLen+1,pLen+1];
        dp[0,0] = true;

        if(p[0]=='*')
        {
            for(int i = 1; i < sLen+1; i++)
            {
                dp[i,1]=true;
            }
            
        }

        for (int i = 1; i < sLen+1; i++)
        {
            for (int j = 1; j < pLen+1; j++)
            {
                if (s[i-1]==p[j-1] || p[j-1]=='?')
                {
                    dp[i,j] = dp[i-1,j-1];
                }
                else if(p[j-1]=='*')
                {
                    dp[i,j] = dp[i,j-1] || dp[i-1,j];
                }
                
            }
        }
        return dp[sLen,pLen];
        
    }
}