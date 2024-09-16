#include <set>
#include <vector>
#include <tuple>
#include <pair>
using namespace std;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) 
    {
        long long ans=0;
        pair<long long,long long> curPos = {0,0};
        pair<long long,long long> nextPos = {0,0};

        //Init obstacles
        set<pair<long long,long long>> newObstacles;
        for (vector<int> obs:obstacles)
        {
            newObstacles.insert({obs[0],obs[1]});
        }
        
        //Init direction
        int direIndex = 0;
        vector<tuple<int,int>> directions;
        
        directions.push_back(make_tuple(0,1));
        directions.push_back(make_tuple(1,0));
        directions.push_back(make_tuple(0,-1));
        directions.push_back(make_tuple(-1,0));

        for (int command:commands)
        {
            switch (command)
            {
                case -1:
                    direIndex = (direIndex+1)%4;
                    break;
                case -2:
                    direIndex = (direIndex+3)%4;
                    break;
                
                default:
                    int remainStep = command;
                    for (int i = 0; i < command; i++)
                    {
                        nextPos = {curPos.first +get<0>(directions[direIndex]),+curPos.second +get<1>(directions[direIndex])};
                        if (newObstacles.find(nextPos)==newObstacles.end())
                        {
                            curPos = nextPos;
                            long long tempDis = curPos.first * curPos.first+ curPos.second * curPos.second;
                            if (tempDis>ans)
                            {
                                ans =tempDis;
                            }
                            remainStep--;
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