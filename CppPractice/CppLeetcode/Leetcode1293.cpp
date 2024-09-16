#include<vector>
#include<deque>
#include<tuple>
#include<map>
using namespace std;

class Solution {
private:
    bool isInRange(int row , int col,int k, const vector<vector<int>> &grid)
    {
        return (row>=0 && row<grid.size() && col>=0 && col<grid[0].size() && k-grid[row][col]>=0);
    };

public:
    int shortestPath(vector<vector<int>> &grid, int k) 
    {
        deque<tuple<int,int,int,int>> theQueue; //Step,row,col,remaining K
        theQueue.push_back(make_tuple(0,0,0,k));
        vector<pair<int,int>> directions = {{0,1},{0,-1},{1,0},{-1,0}};
        map<pair<int,int>,int> visited; // {row,col},k

        while(!theQueue.empty())
        {
            tuple<int,int,int,int> curTuple = theQueue.front();
            int curStep = get<0>(curTuple);
            int curRow = get<1>(curTuple);
            int curCol = get<2>(curTuple);
            int curK = get<3>(curTuple);
            theQueue.pop_front();
            if (curRow ==grid.size()-1 && curCol == grid[0].size()-1)
            {
                return curStep;
            }
            visited[{curRow,curCol}] = curK;
            for (const auto &dire:directions)
            {
                if (isInRange(curRow+dire.first,curCol+dire.second,curK,grid))
                {
                    pair<int,int> newPos = {curRow+dire.first,curCol+dire.second} ;
                    int newK = curK-grid[curRow+dire.first][curCol+dire.second];
                    if (visited.find(newPos)==visited.end() || newK > visited[newPos]) //This is crutial for improving speed
                    {
                        visited[newPos] = newK;
                        theQueue.push_back(make_tuple(curStep+1,newPos.first,newPos.second,newK));
                    }
                }
            }
        }
        return -1;
    }
};