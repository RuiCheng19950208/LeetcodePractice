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
    vector<vector<int>> levelOrder(TreeNode* root) {

        vector<vector<int>> ans;
        if (!root)
        {
            return ans;
        }
        vector<int> level_list;
        vector<TreeNode*> node_list;
        vector<TreeNode*> temp_node_list;

        node_list.push_back(root);
        ans.push_back({root->val});
        while (node_list.size()>0)
        {
            level_list = {};
            temp_node_list = {};
            for (int i = 0; i < node_list.size(); i++)
            {
                if (node_list[i]->left)
                {
                    temp_node_list.push_back(node_list[i]->left);
                }
                if (node_list[i]->right)
                {
                    temp_node_list.push_back(node_list[i]->right);
                }
               
            }
            for (int i = 0; i < temp_node_list.size(); i++)
            {
                level_list.push_back(temp_node_list[i]->val);
            }
            node_list = temp_node_list;
            if (level_list.size()>0)
            {
                ans.push_back(level_list);
            }
           

        }
        return ans;
    }
};