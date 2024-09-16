#include<vector>
#include<tuple>
#include<string>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) 
    {
        vector<vector<string>> finalAns;
        vector<string> board(n,string(n,'.'));

        vector<int> colFeature;
        vector<int> rowPlusColFeature;
        vector<int> rowMinusColFeature;

        dfs(0,n,board,finalAns,colFeature,rowPlusColFeature,rowMinusColFeature);

        return finalAns;
        
    }
private:
    void dfs(
        int rowNum, 
        int nNum, 
        vector<string> &board,
        vector<vector<string>> &finalAns,
        vector<int> &colFeature,
        vector<int> &rowPlusColFeature,
        vector<int> &rowMinusColFeature)
        {
            if (rowNum == nNum)
            {
                finalAns.push_back(board);
                return;
            }
            for (int j = 0; j < nNum; j++) //Go over each column
            {
                if (checkValid(rowNum,j,colFeature,rowPlusColFeature,rowMinusColFeature)==false)
                {
                        continue;
                }
                board[rowNum][j] ='Q'; //Place Q
                colFeature.push_back(j);
                rowPlusColFeature.push_back(rowNum+j);
                rowMinusColFeature.push_back(rowNum-j);

                dfs(rowNum+1,nNum,board,finalAns,colFeature,rowPlusColFeature,rowMinusColFeature);

                board[rowNum][j] ='.'; //undo Q
                colFeature.pop_back();
                rowPlusColFeature.pop_back();
                rowMinusColFeature.pop_back();
            }
            return;
        }

    bool checkValid(
        int i, 
        int j, 
        vector<int> colFeature, 
        vector<int> rowPlusColFeature, 
        vector<int> rowMinusColFeature)
        {
            if (find(colFeature.begin(),colFeature.end(),j)!=colFeature.end() || 
            find(rowPlusColFeature.begin(),rowPlusColFeature.end(),i+j)!=rowPlusColFeature.end()  || 
            find(rowMinusColFeature.begin(),rowMinusColFeature.end(),i-j)!=rowMinusColFeature.end())
            {
                return false;
            }
            return true;
        }
};