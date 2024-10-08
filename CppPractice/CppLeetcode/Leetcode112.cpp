 
class Solution {
public:
    int target; 
    bool helper(TreeNode *node,int temp)
    {
        if(!node->left && !node->right){return temp+node->val==target;}
        else if(!node->left){return helper(node->right,temp+node->val);}
        else if(!node->right){return helper(node->left,temp+node->val);}
        else{return helper(node->left,temp+node->val)||helper(node->right,temp+node->val);}

    }
    bool hasPathSum(TreeNode* root, int targetSum) 
    {
        if(!root){return false;}
        target = targetSum;
        return helper(root,0);
    }
};