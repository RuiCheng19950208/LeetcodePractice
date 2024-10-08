class Solution {
public:
    int minLength(string s) 
    {
        vector<int> theStack;
        for(int i=0;i<s.size();i++)
        {
            
            if(theStack.size()>0&&((s[i]=='B'&&theStack.back()=='A')||(s[i]=='D'&&theStack.back()=='C')))
            {
                theStack.pop_back();
            }
            else
            {
                theStack.push_back(s[i]);
            }
        }
        return theStack.size();
    }
};