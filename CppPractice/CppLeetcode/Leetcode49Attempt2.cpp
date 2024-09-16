#include<vector>
#include<algorithm>
#include<map>
#include<string>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        map<string,vector<string>> theMap;
        for (string s:strs)
        {
            string temp = s;
            sort(temp.begin(),temp.end());
            theMap[temp].push_back(s);
        }
        vector<vector<string>> result;
        for (auto pair:theMap)
        {
            result.push_back(pair.second);
        }
        return result;
    }
};