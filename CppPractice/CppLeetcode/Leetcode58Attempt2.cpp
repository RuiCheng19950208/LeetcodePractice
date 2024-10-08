class Solution {
public:
    int lengthOfLastWord(string s) 
    {
        int ans=0;
        bool isReset = false;
        for(char c:s)
        {
            if(c==' '){isReset =true;}
            else
            {
                if(isReset)
                {
                    isReset=false;
                    ans=1;
                }
                else
                {
                    ans++;
                }
            }
        }
        return ans;
    }
};