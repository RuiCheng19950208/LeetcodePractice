#include<string>
#include<vector>
#include<map>
#include<set>
using namespace std;


class Solution {
public:
    bool isIsomorphic(string s, string t) 
    {
        map<char,char> theMap;
        set<char> seenSet;
        if (s.size()!=t.size())
        {
            return false;
        }
        
        
        for (int i=0;i<s.size();i++)
        {
            if (theMap.find(s[i])==theMap.end())
            {
                theMap[s[i]] = t[i];
                if (seenSet.find(t[i])!=seenSet.end())
                {
                    return false;
                    
                }
                else
                {
                    seenSet.insert(t[i]);
                }
            }
            else if (t[i]!=theMap[s[i]])
            {
                return false;
            }
        }
        return true;
    }
};