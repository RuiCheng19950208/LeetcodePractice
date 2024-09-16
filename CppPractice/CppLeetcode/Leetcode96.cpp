#include<vector>
#include<map>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode():val(0),left(nullptr),right(nullptr){};
    TreeNode(int x):val(x),left(nullptr),right(nullptr){};
    TreeNode(int x, TreeNode *leftp,TreeNode *rightp):val(x),left(leftp),right(rightp){};
};

class Solution {
private:
    int helper(int l,int r,map<int,int> &dp)
    {
        int res=0;
        if (dp.find(r-l)!=dp.end())
        {
            return dp[r-l];
        }
        else
        {
            for (int i = l; i <= r; i++)
            {
                res +=  helper(l,i-1,,dp) * helper(i+1,r,dp);
            }
            dp[r-l] = res;
            return res
        }
        
    }
public:
    int numTrees(int n) 
    {
        map<int,int> dp;
        dp[0] = 1;
        dp[-1] = 1;
        helper(1,n,dp);
        return dp[n];
    }
};