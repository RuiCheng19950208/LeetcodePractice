#include<set>
#include<vector>
#include<utility>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) 
    {
        set<pair<int,int>> colSet; // col,val
        set<pair<int,int>> rowSet; // row,val
        set<pair<int,int>> boxSet;

        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (board[i][j]!='.')
                {
                    int theVal = int(board[i][j]); 
                    int boxIndex = 3* (i/3) + j/3 ;
                    if (colSet.find({j,theVal})!=colSet.end() ||
                        rowSet.find({i,theVal})!=rowSet.end() ||
                        boxSet.find({boxIndex,theVal})!=boxSet.end())
                    {
                        return false;
                    }
                    colSet.insert({j,theVal});
                    rowSet.insert({i,theVal});
                    boxSet.insert({boxIndex,theVal});
                }
            }
        }
        return true;
    }
};