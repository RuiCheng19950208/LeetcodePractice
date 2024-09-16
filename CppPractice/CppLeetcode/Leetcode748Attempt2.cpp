#include<map>
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) 
    {
        map<char,int> licensePlateMap;
        vector<string> candidateList;
        for (char c:licensePlate) //fulfill licensePlateMap
        {
            if (isupper(c))
            {
                licensePlateMap[tolower(c)]++;
            }
            else if (islower(c))
            {
                licensePlateMap[c]++;
            }
        }

        for (string word:words) //Get candidateList
        {
            bool isCandid = true;
            map<char,int> tempMap;
            for (char c:word)
            {
                tempMap[c]++;
            }
            for(const auto &pair:licensePlateMap)
            {
                if (licensePlateMap.find(pair.first)==licensePlateMap.end() || tempMap[pair.first]<licensePlateMap[pair.first])
                {
                    isCandid = false;
                    break;
                }   
            }
            if (isCandid)
            {
                candidateList.push_back(word);
            }
        }

        // Get final answer
        int shortestLen = 2000;
        string ans;
        for (string word:candidateList)
        {
            if (word.size()<shortestLen)
            {
                shortestLen = word.size();
                ans = word;
            }
        }
        return ans;
        
        

    }

}