#include<string>
#include<map>
#include<vector>
using namespace std;

class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) 
    {
        map<int,int> licenseMap; //ascii,frequency
        vector<string> candidateList;
        string ans;
        int shortestLen = 2000;

        int upperAsciiA = int('A');
        int upperAsciiZ = int('Z');
        int lowerAsciiA = int('a');
        int lowerAsciiZ = int('z');
        int converter = int('a') - int('A');
        for (int i = 0; i < licensePlate.size(); i++) //Initialize licenseMap
        {
            if (int(licensePlate[i])>=upperAsciiA && int(licensePlate[i])<=upperAsciiZ)
            {
                if (licenseMap.find(int(licensePlate[i])+converter)==licenseMap.end())
                {
                    licenseMap[int(licensePlate[i])+converter] = 1;
                }
                else
                {
                    licenseMap[int(licensePlate[i])+converter] +=1;
                }
            }
            else if (int(licensePlate[i])>=lowerAsciiA && int(licensePlate[i])<=lowerAsciiZ)
            {
                if (licenseMap.find(int(licensePlate[i]))==licenseMap.end())
                {
                    licenseMap[int(licensePlate[i])] =1;
                }
                else
                {
                    licenseMap[int(licensePlate[i])] +=1;
                }
            }
        }
        for (int i = 0; i < words.size(); i++) //Select candidate
        {
            map<int,int> tempMap;
             bool isCandid = true;
            for (int j = 0; j < words[i].size(); j++) //Create tempMap
            {
                if (tempMap.find(words[i][j])==tempMap.end())
                {
                    tempMap[int(words[i][j])] = 1;
                }
                else
                {
                    tempMap[int(words[i][j])] += 1;
                }
            }
            for(const auto &asc:licenseMap) //After getting the tempMap
            {
                if (tempMap.find(asc.first)==tempMap.end() || tempMap[asc.first]<licenseMap[asc.first])
                {
                    isCandid = false;
                    break; //skip this word   
                }
            }
            if (isCandid)
            {
                candidateList.push_back(words[i]); //Add into candidate if pass the template test
            }
        }

        //Select shortest candidate
        
        
        for (int i = 0; i < candidateList.size(); i++)
        {
            if (candidateList[i].size()<shortestLen)
            {
                ans = candidateList[i];
                shortestLen = candidateList[i].size();
            }
            
            
        }
        return ans;
        
    }
};