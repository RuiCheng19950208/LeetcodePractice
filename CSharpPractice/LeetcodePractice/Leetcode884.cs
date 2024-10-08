public class Solution884 {
    public string[] UncommonFromSentences(string s1, string s2) {
        List<string> res= new List<string>();
        string[] s1List = s1.Split();
        string[] s2List = s2.Split();
        Dictionary<string,int> dict1 = new Dictionary<string, int>();
        Dictionary<string,int> dict2 = new Dictionary<string, int>();
        for (var i = 0; i < s1List.Length; i++)
        {
            if (!dict1.ContainsKey(s1List[i]))
            {
                dict1[s1List[i]]=1;
            }
            else
            {
                dict1[s1List[i]]++;
            }
        }
        for (var i = 0; i < s2List.Length; i++)
        {
            if (!dict2.ContainsKey(s2List[i]))
            {
                dict2[s2List[i]]=1;
            }
            else
            {
                dict2[s2List[i]]++;
            }
        }
        for (var i = 0; i < s1List.Length; i++)
        {
            string theKey = s1List[i];
            if (dict1[theKey]==1 && !dict2.ContainsKey(theKey))
            {
                res.Add(theKey);
            }
            
        }
        for (var i = 0; i < s2List.Length; i++)
        {
            string theKey = s2List[i];
            if (dict2[theKey]==1 && !dict1.ContainsKey(theKey))
            {
                res.Add(theKey);
                
            }
            
        }
        return res.ToArray();
    }
}