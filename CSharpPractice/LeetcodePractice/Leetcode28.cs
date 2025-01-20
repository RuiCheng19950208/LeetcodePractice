public class Solution28 {
    public int StrStr(string haystack, string needle) 
    {
        if(string.IsNullOrEmpty(needle))
        {
            return 0;
        }
        else
        {
            return haystack.IndexOf(needle);
        }
        
    }
}