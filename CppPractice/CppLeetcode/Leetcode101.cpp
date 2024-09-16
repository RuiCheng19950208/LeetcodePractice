
struct TreeNode
{
    int val;
    TreeNode *left;
    Treenode *right;
    TreeNode():val(0),left(nullptr),right(nullptr){};
    TreeNode(int x):val(x),left(nullptr),right(nullptr){};
    TreeNode(int x,TreeNode *leftp,TreeNode *rightp): val(x),left(leftp),right(rightp){}; 
};

class Solution 
{
private:
    bool helper(TreeNode *p1,TreeNode *p2)
    {
        if ((p1 && !p2) || (!p1 && p2))
        {
            return false;
        }
        else if (!p1 && !p2)
        {
            return true;
        }
        else
        {
            return (p1->val==p2->val && helper(p1->left,p2->right) && helper(p1->right,p2->left));
        }
    }
public:
    bool isSymmetric(TreeNode* root) 
    {
        if (!root)
        {
            return true;
        }
        else
        {
            return helper(root->right,root->left);
        }        
    }
};