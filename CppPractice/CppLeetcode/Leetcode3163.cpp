class Solution {
public:
    string compressedString(string word) 
    {
        string ans="";
        int count = 1;
        char curChar = word[0];
        if (word.size()==1){return "1"+string(1,curChar);}
        for(int i=1;i<word.size();i++)
        {
            if(word[i]==curChar)
            {
                if(count==9)
                {
                    ans+="9";
                    ans+=string(1,curChar);
                    count =1;
                }
                else{count+=1;}
            }
            else
            {
                ans+=to_string(count);
                ans+=string(1,curChar);
                count=1;
                curChar = word[i];
            }
        }
        ans+=to_string(count);
        ans+=string(1,curChar);
        return ans;
    }
};