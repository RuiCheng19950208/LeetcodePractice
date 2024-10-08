public class Solution383 {
    public bool CanConstruct(string ransomNote, string magazine) {
        Dictionary<char,int> dictr = new Dictionary<char, int>();
        Dictionary<char,int> dictm = new Dictionary<char, int>();
        foreach (char c in ransomNote)
        {
            if (dictr.TryGetValue(c, out int count))
            {
                dictr[c]++;
            }
            else
            {
                dictr[c]=1;
            }
        }
        foreach(char c in magazine)
        {
            if (dictm.TryGetValue(c, out int count))
            {
                dictm[c]++;
            }
            else
            {
                dictm[c]=1;
            }
        }
        foreach (var kvp in dictr)
        {
            char c = kvp.Key;
            if (!dictm.ContainsKey(c)||dictr[c]>dictm[c])
            {
                return false;
            }
        }
        return true;
    }
}