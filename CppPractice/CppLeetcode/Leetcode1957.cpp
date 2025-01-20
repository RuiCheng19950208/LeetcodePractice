class Solution {
public:
    string makeFancyString(string s) 
    {
        if(s.size()<3)
        {
            return s;
        }
         
        char curChar = s[0];
        int temp = 1;
        string  ans(1, s[0]);
        for(int i=1;i<s.size();i++)
        {
            if(s[i]==curChar)
            {
                temp+=1;
                if(temp<3)
                {
                    ans+=s[i];
                }

            }
            else
            {
                temp=1;
                curChar = s[i];
                ans+=s[i];

            }
        }


        return ans;
        
    }
};