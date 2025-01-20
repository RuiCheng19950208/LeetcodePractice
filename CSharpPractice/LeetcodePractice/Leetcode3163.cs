using System.Text;
public class Solution3163 {
    public string CompressedString(string word) 
    {
        int count=1;
        char curChar  = word[0];
        StringBuilder ans=  new StringBuilder();

        if(word.Length<2)
        {
            ans.Append(1);
            ans.Append(word[0]);
            return ans.ToString();
        }
        for(int i=1;i<word.Length;i++)
        {
            if(word[i]==curChar)
            {
                if(count==9)
                {
                    ans.Append(9).Append(curChar);
                    count=1;
                }
                else{count+=1;}
            }
            else
            {
                ans.Append(count).Append(curChar);
                count=1;
                curChar = word[i];
            }
        }
        ans.Append(count);
        ans.Append(curChar);
        return ans.ToString();
    }
}