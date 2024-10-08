class Solution {
public:
    int helper(TreeNode *node)
    {
        if(!node){return 0;}
        int leftH = helper(node->left);
        int rightH = helper(node->right);
        if(leftH==-1||rightH==-1||abs(rightH-leftH)>1){return -1;}

        return 1+max(leftH,rightH);
    }
    bool isBalanced(TreeNode* root) {

        if(!root){return true;}
        return helper(root)!=-1;
        
    }
};