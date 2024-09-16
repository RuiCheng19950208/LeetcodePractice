#include<deque>
using namespace std;

class Solution {

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

public:
    bool dfs(ListNode* head, TreeNode *node)
    {
        if (head==nullptr)
        {
            return true;
        }
        if (node==nullptr)
        {
            return false;
        }
        if (head->val != node->val)
        {
            return false;
        }
        return dfs(head->next,node->left) || dfs(head->next,node->right);
    }
    bool isSubPath(ListNode* head, TreeNode* root) 
    {
        deque<TreeNode*> theQueue;
        theQueue.push_back(root);
        theQueue.pop_front();
        while (theQueue.size()>0)
        {
            TreeNode *node = theQueue.front();
            theQueue.pop_front();
            if (dfs(head,node))
            {
                return true;
            }
            else
            {
                if (node->left)
                {
                    theQueue.push_back(node->left);
                }
                if (node->right)
                {
                    theQueue.push_back(node->right);
                }
                
                
            }
            

        }
        return false;
        
    }
};