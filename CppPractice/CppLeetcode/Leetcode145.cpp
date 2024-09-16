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
    void Traversal(TreeNode *p,vector<int> &res)
    {
        if (!p)
        {
            return;
        }
        else
        {
            Traversal(p->left,res);
            Traversal(p->right,res);
            res.push_back(p->val);
        }
    }
public:
    vector<int> postorderTraversal(TreeNode* root) 
    {
        vector<int> result;
        Traversal(root,result);
        return result;
    }
};

