class Solution {
public:
    int ans=1;
    void helper(TreeNode* node,int temp)
    {
        if(!node){return;}
        ans=max(ans,temp);
        helper(node->right,temp+1);
        helper(node->left,temp+1);
        return;
    }
    int maxDepth(TreeNode* root) 
    {
        if(!root){return 0;}
        helper(root,1);
        return ans;
        
    }
};