#include<set>
#include<vector>
#include <utility> 

using namespace std;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) 
    {
        long long ans;
        pair<int,int> curPos = {0,0};
        pair<int,int> nextPos = {0,0};

        //Init directions
        vector<pair<int,int>> directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int direIndex = 0;

        //Init obs
        // set<int> obsXSet;
        // set<int> obsYSet;
        set<pair<int,int>> obsSet;
        for (vector<int> obs:obstacles)
        {
            obsSet.insert({obs[0],obs[1]});
            // obsXSet.insert(obs[0]);
            // obsYSet.insert(obs[1]);
        }

        for (int command:commands)
        {
            switch (command)
            {
            case -1:
                direIndex = (direIndex+1) % 4;
                break;
            case -2:
                direIndex = (direIndex+3) % 4;
                break;
            
            default:
                for (int i = 0; i < command; i++)
                {
                    nextPos = {curPos.first +directions[direIndex].first, curPos.second +directions[direIndex].second};
                    if (obsSet.find(nextPos)==obsSet.end())
                    {
                        curPos = nextPos;
                        int tempVal = curPos.first * curPos.first + curPos.second * curPos.second;
                        if (tempVal>ans)
                        {
                            ans=tempVal;
                        }
                    }
                    else
                    {
                        break;
                    }
                }
                break;
            }
        }
        return ans;

    }
};