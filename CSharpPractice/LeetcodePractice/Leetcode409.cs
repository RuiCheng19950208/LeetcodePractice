public class Solution409 {
    public int LongestPalindrome(string s) {
        bool isPlus = false;
        int ans = 0;
        Dictionary<char,int> theDict = new Dictionary<char, int>();
        foreach (char c in s)
        {
            if (!theDict.ContainsKey(c))
            {
                theDict[c]=1;
            }
            else
            {
                theDict[c]+=1;
            }
        }
        foreach (KeyValuePair<char,int> pair in theDict)
        {
            if (pair.Value%2==1)
            {
                isPlus=true;
            }
            ans+=2*(pair.Value/2);
        }
        if (isPlus)
        {
            ans+=1;
        }
        return ans;
    }
}