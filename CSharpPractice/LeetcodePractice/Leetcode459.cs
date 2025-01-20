public class Solution459 {
    public bool RepeatedSubstringPattern(string s) 
    {
        string ds =s+s;
        string sub = ds.Substring(1,ds.Length-2);
        return sub.Contains(s);
    }
}