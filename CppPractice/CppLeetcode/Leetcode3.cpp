#include <map>
#include <string>
#include <iostream>



using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        int maxLength = 0;
        int start = 0;
        map<char,int> theMap;
        for (int i = 0; i < s.length(); i++)
        {
            if (theMap.find(s[i])!=theMap.end())
            {
                start = theMap[s[i]] + 1;
            }
            
            theMap[s[i]] = i;
            maxLength =max(maxLength, i - start);
            
            
        }
        for(const auto &pair:theMap)
        {
            cout<<pair.first<<" "<<pair.second<<endl;
        }

        

        return maxLength;
    }
};