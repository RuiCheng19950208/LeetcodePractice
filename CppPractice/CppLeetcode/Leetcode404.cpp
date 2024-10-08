struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    
    TreeNode():val(0),right(nullptr),left(nullptr){}
    TreeNode(int v):val(v),right(nullptr),left(nullptr){}
    TreeNode(int v, TreeNdoe *l,TreeNode*r):val(0),right(r),left(l){}

}

class Solution {
public:
    int helper(TreeNode* node,bool flag)
    {
        if (node==nullptr)
        {
            return 0;
        }
        if (node->left==nullptr && node->right==nullptr && flag)
        {
            return node->val;
        }
        else
        {
            return helper(node->left,true)+helper(node->right,false);
        }


    }
    int sumOfLeftLeaves(TreeNode* root) {
        return helper(root->right,false)+helper(root->left,true);
    }
};