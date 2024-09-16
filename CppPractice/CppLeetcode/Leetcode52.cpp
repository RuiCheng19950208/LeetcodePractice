#include<set>
using namespace std;

class Solution {
public:
    int publicN=0; 
    int ans=0;
    set<int> colSet;
    set<int> PlusSet;
    set<int> MinusSet;
    bool isValid(int i,int j)
    {
        if (colSet.find(j)!=colSet.end() || PlusSet.find(i+j)!=PlusSet.end() ||MinusSet.find(i-j)!=MinusSet.end())
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    void dfs(int i)
    {
        if (i==publicN)
        {
            ans++;
        }
        else
        {
            for (int j = 0; j < publicN; j++)
            {
                if (isValid(i,j))
                {
                    colSet.insert(j);
                    PlusSet.insert(i+j);
                    MinusSet.insert(i-j);

                    dfs(i+1);
                    
                    colSet.erase(j);
                    PlusSet.erase(i+j);
                    MinusSet.erase(i-j);
                }
            }
        }
    }
    int totalNQueens(int n)
    {
        publicN = n;
        dfs(0);
        return ans;
    }
};