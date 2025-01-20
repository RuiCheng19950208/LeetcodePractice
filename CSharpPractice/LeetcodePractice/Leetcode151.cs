public class Solution151 {
    public string ReverseWords(string s) 
    {
        string temp="";
        List<string> wordList = new List<string>();
        for(int i=0;i<s.Length;i++)
        {
            if(s[i]!=' ')
            {
                temp += s[i];
            }
            else if(temp.Length>0)
            {
                wordList.Add(temp);
                temp="";
            }
        }
        if(temp.Length>0){wordList.Add(temp);}
        wordList.Reverse();
        return string.Join(" ",wordList);
    }
}