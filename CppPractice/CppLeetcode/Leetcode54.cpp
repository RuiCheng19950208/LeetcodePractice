#include <vector>
using namespace std;
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) 
    {
        vector<int> res;
        int rowNum = matrix.size();
        int colNum = matrix[0].size();
        int step = rowNum*colNum; 

        vector<vector<bool>> visited(m,vector<bool>(n,false));

        int curRow = 0;
        int curCol = 0;
        int directIndex = 0;
        vector<pair<int,int>> directions;
        directions.push_back(make_pair(0,1));
        directions.push_back(make_pair(1,0));
        directions.push_back(make_pair(0,-1));
        directions.push_back(make_pair(-1,0));

        while (step>0)
        {
            res.push_back(matrix[curRow][curCol]);
            step--;

            int nextRow = curRow + directions[directIndex].first;
            int nextCol = curRow + directions[directIndex].second;
            if(nextRow<0||nextCol<0||nextRow>m-1||nextCol>n-1||visited[nextRow][nextCol]==true)
            {
                directIndex = (directIndex+1)%4;
                cur = curRow + directions[directIndex].first;
                cur = curRow + directions[directIndex].second;
            }

        }
        return res;
    }
};