#include<map>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
private:
    vector<char> split(string s)
    {
        vector<char> result;
        for(char c:s)
        {
            result.push_back(c);
        }
        return result;
    }

    vector<char> sortString(vector<char> cList)
    {

        sort(cList.begin(),cList.end());
        return cList;
    }

    string joinString(vector<char> cList)
    {
        string result = "";
        for (char c:cList)
        {
            result += c;
        }
        
        return result;
    }
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        vector<vector<string>> result;
        map<string,vector<string>> theDict;
        for (string s:strs)
        {
            string temp = joinString(sortString(split(s)));
            if (theDict.find(temp)!=theDict.end())
            {
                theDict[temp].push_back(s);
            }
            else
            {
                theDict[temp] = {s};
            }
        }
        for(const auto &pair:theDict)
        {
            result.push_back(pair.second);
        }
        return result;
        
    }
};