using System.Text;
public class Solution1957 {
    public string MakeFancyString(string s) 
    {
        if(s.Length<3){return s;}
        StringBuilder ans = new StringBuilder();
        ans.Append(s[0]);
        int temp=1;
        char curChar = s[0];
        for (int i=1;i<s.Length;i++)
        {
            if(s[i]==curChar)
            {   
                temp+=1;
                if(temp<3)
                {
                    ans.Append(s[i]);
                }
            }
            else
            {
                temp=1;
                curChar = s[i];
                ans.Append(s[i]);

            }
        }
        return ans.ToString();
        
    }
}