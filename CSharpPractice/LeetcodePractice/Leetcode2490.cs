public class Solution2490 {
    public bool IsCircularSentence(string sentence) 
    {
        string[] sList = sentence.Split(" ");
        int n = sList.Length;
        for(int i=0;i<n-1;i++)
        {
            if(sList[i][sList[i].Length-1]!=sList[i+1][0])
            {
                return false;
            }
        }
        if(sList[0][0]!=sList[n-1][sList[n-1].Length-1])
        {
            return false;
        }
        return true;
    }
}