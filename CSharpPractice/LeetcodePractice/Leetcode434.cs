public class Solution434 {
    public int CountSegments(string s) {
        int ans=0;
        for (var i = 0; i < s.Length; i++)
        {
            if (s[i]!=' ' &&(s[i-1]==' ' || s[0]!=' '))
            {
                ans++;
            }
        }
        return ans;
        
    }
}