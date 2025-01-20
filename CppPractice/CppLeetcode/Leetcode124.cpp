class Solution {
public:
    int ans =-10000;
    int helper(TreeNode *node)
    {
        if(!node){return 0;}
        int rightSum = max(0,helper(node->right));
        int leftSum = max(0,helper(node->left));
        int tempAns = node->val + rightSum+leftSum;
        ans = max(ans,tempAns);
        return node->val+max(rightSum,leftSum);

    }
    int maxPathSum(TreeNode* root) {
        helper(root);
        return ans;
    }
};