class Solution {
public:
    string helper(string curString,int n)
    {
        if(n==1)
        {
            return curString;
        }
        else
        {
            string newString="";
            char curChar=curString[0];
            int curCharCount =1;
            for(int i=1;i<curString.size();i++)
            {
                if(curString[i]!=curString[i-1])
                {
                    newString += to_string(curCharCount)+curChar;
                    curChar = curString[i];
                    curCharCount =1;
                }
                else
                {
                    curCharCount++;
                }

            }
            newString += to_string(curCharCount)+curChar;
            return helper(newString,n-1);
        }

    }
    string countAndSay(int n) 
    {
        return helper("1",n);
        
    }
};