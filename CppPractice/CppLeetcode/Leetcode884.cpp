#include<vector>
#include<map>
using namespace std;
class Solution {
private:
    vector<string> splitString(string s, char delimiter)
    {
        vector<string> res;
        stringstream ss(s);
        string item;
        while(getline(ss,item,delimiter))
        {
            res.push_back(item);
        }

        return res;
    }




public:
    vector<string> uncommonFromSentences(string s1, string s2) 
    {
        vector<string> ans;
        map<string,int> dict1;
        map<string,int> dict2;
        vector<string> sList1 = splitString(s1,' ');
        vector<string> sList2 = splitString(s2,' ');
        for(int i = 0; i < sList1.size(); i++)
        {
            if (dict1.find(sList1[i])==dict1.end())
            {
                dict1[sList1[i]] = 1;
                
            }
            else
            {
                dict1[sList1[i]] ++;
            }
        }
        for(int i = 0; i < sList2.size(); i++)
        {
            if (dict2.find(sList2[i])==dict2.end())
            {
                dict2[sList2[i]] = 1;
                
            }
            else
            {
                dict2[sList2[i]] ++;
            }
        }
        for(int i = 0; i < sList1.size(); i++)
        {
            if (dict1[sList1[i]] ==1 and dict2.find(sList1[i])==dict2.end())
            {
                ans.push_back(sList1[i]);
            }
        }
        for(int i = 0; i < sList2.size(); i++)
        {
            if (dict2[sList2[i]] ==1 and dict1.find(sList2[i])==dict1.end())
            {
                ans.push_back(sList2[i]);
            }
        }
        return ans;        
    }
};

