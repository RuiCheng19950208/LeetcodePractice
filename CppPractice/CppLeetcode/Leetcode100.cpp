#include<iostream>
using namespace std;


struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(): val(0),left(nullptr),right(nullptr){};
    TreeNode(int x): val(x),left(nullptr),right(nullptr){};
    TreeNode(int x,TreeNode *leftp,TreeNode *rightp): val(x),left(leftp),right(rightp){};
};
class Solution 
{
private:
    bool helper(TreeNode *p1, TreeNode *p2)
    {
        if ((!p1 && p2) ||(p1 && !p2) || (p1->val!=p2->val))
        {
            return false;
        }
        else if (!p1 && !p2)
        {
            return true;
        }   
        else
        {
            return p1->val==p2->val && helper(p1->left,p2->left) && helper(p1->right,p2->right);
        }
    }
public:
    bool isSameTree(TreeNode* p, TreeNode* q) 
    {
        return helper(p,q);
    }
};