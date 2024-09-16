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
    vector<TreeNode*> node_list;

    void DFS(TreeNode* root) {
        if (!root)
        {
            return;
        }
        node_list.push_back(root);
        if (root->left)
        {
            DFS(root->left);
        }
        if (root->right)
        {
            DFS(root->right);
        }
    }
    void flatten(TreeNode* root) {
        if (!root)
        {
            return;
        }
        TreeNode* cur = root;
        vector<int> val_list;

        vector<TreeNode*> temp_node_list;
        DFS(cur);
        for (int i = 0; i < node_list.size(); i++)
        {
            val_list.push_back(node_list[i]->val);

        }

        // This is BFS which is totally wrong in this case.We need DFS
        //while (node_list.size()>0)
        //{
        //    temp_node_list = {};
        //    for (int i = 0; i < node_list.size(); i++)
        //    {
        //        val_list.push_back(node_list[i]->val);
        //        if (node_list[i]->left)
        //        {
        //            temp_node_list.push_back(node_list[i]->left);
        //        }
        //        if (node_list[i]->right)
        //        {
        //            temp_node_list.push_back(node_list[i]->right);
        //        }
        //    }
        //    node_list = temp_node_list;
        //}
        //for (int i = 0; i < val_list.size(); i++)
        //{
        //    cout << val_list[i] << endl;
        //}

        cur->left = NULL;
        cur->val = val_list[0];
        if (val_list.size() > 1)
        {
            for (int i = 1; i < val_list.size(); i++)
            {
                cur->right = new TreeNode(val_list[i]);
                cur = cur->right;
            }
        }

    }
};