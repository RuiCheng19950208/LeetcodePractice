public class Solution1593 {
    public HashSet<string> theSet = new HashSet<string>();
    public string theS;
    public int n;

    public int helper(int start)
    {
        if(start==n){return theSet.Count;}
        int ans=0;
        for(int end=start+1;end<n+1;end++)
        {
            string curString =theS.Substring(start,end-start);
            if(!theSet.Contains(curString))
            {
                theSet.Add(curString);
                ans=Math.Max(ans,helper(end));
                theSet.Remove(curString);
            }
        }
        return ans;
    }
    public int MaxUniqueSplit(string s) 
    {
        theS=s;
        n=s.Length;
        return helper(0);
    }
}