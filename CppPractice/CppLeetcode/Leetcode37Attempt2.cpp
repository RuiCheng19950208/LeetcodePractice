#include<vector>

using namespace std;
class Solution {
private:
    bool isValid(int row,int col, char c,vector<vector<char>> &board)
    {
        for (int i = 0; i < 9; i++)
        {
            if (board[row][i]==c || board[i][col]==c || board[3*(row/3)+i/3][3*(col/3)+i%3]==c)
            {
                return false;
            }
        }
        return true;
    }
    bool dfs(int row,int col,vector<vector<char>> &board)
    {
        if (row==9)
        {
            return true;
        }
        if (col==9)
        {
            return dfs(row+1,0,board);
        }
        if (board[row][col]!='.')
        {
            return dfs(row,col+1,board);
        }
        else
        {
            for (char c = '1'; c <='9'; c++)
            {
                if (isValid(row,col,c,board))
                {
                    board[row][col] = c;
                    if (dfs(row,col+1,board))
                    {
                        return true;
                    }
                     board[row][col] = '.';
                }  
            }
        }
        return false;
    }
public:
    void solveSudoku(vector<vector<char>>& board) 
    {
        dfs(0,0,board);
        return;
    }
};