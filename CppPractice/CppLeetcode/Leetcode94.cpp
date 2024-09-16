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
    void InOrderTraversal(TreeNode *p, vector<int> &res)
    {
        if(!p)
        {
            return;
        }
        else
        {
            InOrderTraversal(p->left,res);
            res.push_back(p->val);
            InOrderTraversal(p->right,res);
        }
    }
public:
    vector<int> inorderTraversal(TreeNode* root) 
    {
        vector<int> result;
        InOrderTraversal(root,result);
        return result;
    }
};