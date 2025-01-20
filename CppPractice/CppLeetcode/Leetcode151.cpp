class Solution {
public:
    string reverseWords(string s) 
    {
        vector<string> wordList;
        string temp;
        string ans;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!=' '){temp+=s[i];}
            else if(temp.size()>0)
            {
                wordList.push_back(temp);
                temp="";
            }
        }
        if(temp.size()>0){wordList.push_back(temp);}
        int n = wordList.size();
        for(int i=0;i<n;i++)
        {
            ans+= wordList[n-1-i];
            if(i!=n-1)
            {
                ans+=" ";
            }
        }
        return ans;
    }
};