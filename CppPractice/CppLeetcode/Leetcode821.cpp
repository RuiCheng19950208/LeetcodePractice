#include<cmath>
#include<vector>
#include<string>

using namespace std;

class Solution 
{
public:
    vector<int> shortestToChar(string s, char c) 
    {
        vector<int> result;
        vector<int> candidIndexList;
        int prevDis = 0;
        for (int i = 0; i < s.length(); i++)
        {
           if (s[i]==c)
           {
             candidIndexList.push_back(i);
           }
           
        }
        
        for (int i = 0; i < s.length(); i++)
        {
            prevDis = pow(2,10);
            for (int &j:candidIndexList)
            {
                if (abs(i-j) < prevDis)
                {
                    prevDis = abs(i-j);
                }
                else
                {
                    break;
                }
            }
            result.push_back(prevDis);
        }
        return result;
    }
};