#include "LeetcodeHeader.h"

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
    
};
class Solution {
public:
    int depth_node(TreeNode* Node) {
        if (Node == NULL) 
        {
            return 0;
        }
        else
        {
            return max(depth_node(Node->left),depth_node(Node->right)) + 1;
        }
    
    
    }
    bool isBalanced(TreeNode* root) {
        if (!root)
        {
            return true;
        }
        if (abs(depth_node(root->left)-depth_node(root->right))<2)
        {
            return isBalanced(root->left) and isBalanced(root->right);
        }
        else
        {
            return false;
        }


    }
};