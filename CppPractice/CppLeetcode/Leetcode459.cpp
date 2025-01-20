
class Solution {
public:
    bool repeatedSubstringPattern(string s) 
    {
        string ds=s+s;
        string sub  = ds.substr(1,ds.size()-2);
        return sub.find(s)!=string::npos;
    }
};