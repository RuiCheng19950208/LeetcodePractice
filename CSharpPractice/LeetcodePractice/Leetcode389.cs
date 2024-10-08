public class Solution389 {
    public char FindTheDifference(string s, string t) {
        Dictionary<char,int> dicts = new Dictionary<char, int>();
        Dictionary<char,int> dictt = new Dictionary<char, int>();
        foreach (char c in s)
        {
            if(dicts.TryGetValue(c, out int count))
            {
                dicts[c] ++;
            }
            else
            {
                dicts[c] =1;
            }
            
        }
        foreach (char c in t)
        {
            if(dictt.TryGetValue(c, out int count))
            {
                dictt[c] ++;
            }
            else
            {
                dictt[c] =1;
            }
        }
        foreach (char c in t)
        {
            if (!dicts.ContainsKey(c) || dictt[c]>dicts[c])
            {
                return c;
            }
        }
        return '0';
    }
}