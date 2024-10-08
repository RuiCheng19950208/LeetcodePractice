public class Solution392 {
    public bool IsSubsequence(string s, string t) {
        int fast = 0;
        int slow=0;
        if (s.Length==0)
        {
            return true;
        }
        if (t.Length==0)
        {
            return false;
        }
        while (fast<t.Length)
        {
            if (s[slow]==t[fast])
            {
                slow++;
                fast++;
            }
            else
            {
                fast++;
            }
            if (slow>=s.Length)
            {
                return true;
            }
        }
        return false;
        
    }
}