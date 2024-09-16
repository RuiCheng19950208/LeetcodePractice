#include<vector>
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
    vector<TreeNode*> helper(int leftIndex,int rightIndex)
    {
        vector<TreeNode*> res; //Has to defined out side of for loop
        if (leftIndex>rightIndex)
        {
            res.push_back(nullptr);
            return res;
        }
        else
        {
            for (int i = leftIndex; i <= rightIndex; i++)
            {
                for (TreeNode* leftBranch:helper(leftIndex,i-1))
                {
                    for (TreeNode* rightBranch:helper(i+1,rightIndex))
                    {
                        res.push_back(new TreeNode(i,leftBranch,rightBranch));
                    }
                }
            }
            return res;
        }
    }
public:
    vector<TreeNode*> generateTrees(int n) 
    {
        vector<TreeNode*> res;
        res = helper(1,n);
        return res;   
    }
};