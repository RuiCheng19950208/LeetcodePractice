public class Solution2914 {
    public int MinChanges(string s) 
    {
        int ans=0;
        for(int i=1;i<s.Length;i+=2)
        {
            if(s[i]!=s[i-1]){ans++;}
        }
        return ans;
        
    }
}