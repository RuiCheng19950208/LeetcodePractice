#include<utility>
#include<vector>

using namespace std;

class Solution {
private:
    bool dfs(
        int row,
        int col,
        vector<pair<int,char>> &rowVec,
        vector<pair<int,char>> &colVec,
        vector<pair<int,char>> &boxVec,
        vector<vector<char>> &board)
        {

            if (row==9)
            {
                return true;
            }
            if (col==9)
            {
                return dfs(row+1,0,rowVec,colVec,boxVec,board);
            }
            if (board[row][col]!='.')
            {
                return dfs(row,col+1,rowVec,colVec,boxVec,board);
            }
            else
            {

                for (char c = '1'; c <= '9'; c++)
                {
                    if (isValid(row,col,c,rowVec,colVec,boxVec))
                    {
                        rowVec.push_back({row,c});
                        colVec.push_back({col,c});
                        boxVec.push_back({3*(row/3)+col/3,c});
                        board[row][col] =c;
                        if (dfs(row,col+1,rowVec,colVec,boxVec,board))
                        {
                            return true;
                        }
                        rowVec.pop_back();
                        colVec.pop_back();
                        boxVec.pop_back();
                        board[row][col] ='.';
                    }
                }
            }
            return false;
        }
private:
    bool isValid(
    int row,
    int col,
    char val,
    vector<pair<int,char>> &rowVec,
    vector<pair<int,char>> &colVec,
    vector<pair<int,char>> &boxVec)
    {
        if (find(rowVec.begin(), rowVec.end(), make_pair(row, val)) != rowVec.end())
        {
            return false;
        }
        if (find(colVec.begin(), colVec.end(), make_pair(col, val)) != colVec.end())
        {
            return false;
        }

        int boxRow = row / 3;
        int boxCol = col / 3;
        int boxIndex = 3 * boxRow + boxCol;

       
        if (find(boxVec.begin(), boxVec.end(), make_pair(boxIndex, val)) != boxVec.end())
        {
            return false;
        }
        
        return true;
    }
public:
    void solveSudoku(vector<vector<char>>& board) 
    {

        //Initalize vector
        vector<pair<int,char>> rowVec;
        vector<pair<int,char>> colVec;
        vector<pair<int,char>> boxVec;

        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (board[i][j]!='.')
                {
                    rowVec.push_back({i,board[i][j]});
                    colVec.push_back({j,board[i][j]});
                    boxVec.push_back({3*(i/3)+j/3,board[i][j]});
                }
            }
        }
        //run dfs
        dfs(0,0,rowVec,colVec,boxVec,board);
        return;
    }
};