#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

using namespace std;

class Solution {
public:
    int can_attack(int begin, int end, vector<vector<char>>& board, bool is_row, vector<int> coor)
    {
        if (is_row == true && begin < end)
        {
            for (int i = begin; i < end; i++)
            {
                if (board[i][coor[1]] == 'p')
                {
                    return 1;

                }
                else if (board[i][coor[1]] == 'B')
                {
                    return 0;

                }


            }

        }
        else if (is_row == true)
        {
            for (int i = begin; i >= end; i--)
            {
                if (board[i][coor[1]] == 'p')
                {
                    return 1;

                }
                else if (board[i][coor[1]] == 'B')
                {
                    return 0;

                }

            }

        }
        else if (is_row == false && begin < end)
        {
            for (int i = begin; i < end; i++)
            {
                if (board[coor[0]][i] == 'p')
                {
                    return 1;

                }
                else if (board[coor[0]][i] == 'B')
                {
                    return 0;

                }

            }

        }
        else
        {
            for (int i = begin; i >= end; i--)
            {
                if (board[coor[0]][i] == 'p')
                {
                    return 1;

                }
                else if (board[coor[0]][i] == 'B')
                {
                    return 0;

                }

            }

        }

        return 0;


    };
    int numRookCaptures(vector<vector<char>>& board) {
        vector<int> coor;
        int ans = 0;
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (board[i][j] == 'R')
                {
                    coor.push_back(i);
                    coor.push_back(j);
                }
            }
        }

        ans += can_attack(coor[0], 0, board, true, coor);
        ans += can_attack(coor[0], board.size(), board, true, coor);
        ans += can_attack(coor[1], 0, board, false, coor);
        ans += can_attack(coor[1], board[1].size(), board, false, coor);
        return ans;
    }


};

