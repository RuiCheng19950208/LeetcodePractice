

public class Solution49 {
    public IList<IList<string>> GroupAnagrams(string[] strs) 
    {
        Dictionary<string,List<string>> theMap = new Dictionary<string,List<string>>();
        foreach (string s in strs)
        {
            char[] charArray = s.ToCharArray();
            Array.Sort(charArray); 
            string temp = new string(charArray);
            if (!theMap.ContainsKey(temp))
            {
                theMap[temp] = new List<string>();
            }
            theMap[temp].Add(s);
        }

        IList<IList<string>> result = new List<IList<string>>();
        foreach (var pair in theMap)
        {
            result.Add(pair.Value);
        }
        return result;
        
    }
}