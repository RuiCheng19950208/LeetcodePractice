using System.Diagnostics.Contracts;

public class Solution32 {
    public int LongestValidParentheses(string s) {
        List<int> stack = new List<int>(-1);
        int ans=0;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i]=='(')
            {
                stack.Add(i);
            }
            else
            {
                stack.RemoveAt(stack.Count-1);
                if (stack.Count==0)
                {
                    stack.Add(i);
                }
                else
                {
                    ans= Math.Max(ans, i-stack[stack.Count-1]);
                }
            }
        }
        return ans;
    }
}