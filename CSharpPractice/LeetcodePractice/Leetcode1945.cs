public class Solution1945 {
    public int GetLucky(string s, int k) 
    {
        string covertedString = "";
        foreach (char c in s)
        {
            covertedString += (c-'a'+1).ToString();
        }
        int theSum = 0;
        while (k>0)
        {
            foreach (char c in covertedString)
            {
                theSum += c-'a'+1;
            }
            covertedString = theSum.ToString();

            k--;
            
        }
        return int.Parse(covertedString);
        
    }
}