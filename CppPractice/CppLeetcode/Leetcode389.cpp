#include <map>
class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char,int> dicts;
        map<char,int> dictt;
        for(auto c : s)
        {
            dicts[c] ++;
        }
        for(auto c : t)
        {
            dictt[c] ++;
        }
        for(auto c : t)
        {
            if (dictt[c]>dicts[c])
            {
                return c;
            }
        }
        return '0';
    }
};