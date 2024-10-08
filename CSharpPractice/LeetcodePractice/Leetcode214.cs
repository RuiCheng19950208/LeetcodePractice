using System.Numerics;

public class Solution214 {
    private int[] KMP(string s)
    {
        int[] ans = new int[s.Length];
        int slow = 0;
        int fast = 1;
        while (fast<s.Length)
        {
            if (s[fast] ==s[slow])
            {
                slow++;
                ans[fast]=slow;
                fast++;
            }
            else
            {
                if (slow!=0)
                {
                    slow = ans[slow-1];
                }
                else
                {
                    ans[fast] = 0;
                    fast++;
                }
            }
        }
        return ans;
    }
    public string ShortestPalindrome(string s) {
        string reverseS = s;
        reverseS = new string(reverseS.Reverse().ToArray());
        string mergeS = s+" " +reverseS;
        int[] KMPList = KMP(s);

        return reverseS.Substring(0,reverseS.Length-KMPList[KMPList.Length-1]) +s;
        
    }
}