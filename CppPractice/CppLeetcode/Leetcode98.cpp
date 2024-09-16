#include<limits>
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

class Solution 
{
private:
    bool helper(TreeNode *p,double leftBound,double rightBound)
    {
        if (!p)
        {
            return true;
        }
        else if (p->val<=leftBound || p->val>=rightBound)
        {
            return false;
        }
        else
        {
            return (helper(p->left,leftBound,p->val) && helper(p->right,p->val,rightBound));
        }
        
        
        
    }
public:
    bool isValidBST(TreeNode* root) {
        double intRightBound = numeric_limits<double>::infinity();
        double intLeftBound = -numeric_limits<double>::infinity();
        if (!root)
        {
            return true;
        }
        else
        {
            return helper(root,intLeftBound,intRightBound);
        }
    }
};