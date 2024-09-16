#include<vector>
#include<iostream>
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

class Solution 
{
private:
    void pushLeft(TreeNode* node,vector<TreeNode*> &stack)
    {
        if (node)
        {   
            stack.push_back(node);
            if (node->left)
            {
                pushLeft(node->left,stack);
            }   
        }
    }

public:
    void recoverTree(TreeNode* root) 
    {
        TreeNode* first=nullptr; //Have to initialize pointers to nullptr
        TreeNode* second=nullptr;
        TreeNode* curNode=nullptr;
        TreeNode* preNode =nullptr;
        vector<TreeNode*> theStack;
        int counter = 0 ; 
        
        pushLeft(root,theStack);
        while (theStack.size())
        {
            preNode = curNode;
            curNode = theStack.back();
            theStack.pop_back();
            if (curNode->right)
            {
                pushLeft(curNode->right,theStack);
            }
            if (preNode)
            {
                // cout<<(to_string(curNode->val)+"cur")<<endl;
                // cout<<(to_string(preNode->val)+"pre")<<endl;
                if (curNode->val < preNode->val) // curNode->val < preNode->val can only happended twice or less. use counter to determine if it is the first time or the second time.
                {
                    if (counter == 0)
                    {
                        first  = preNode;
                        second = curNode;
                        counter = 1;
                    }
                    else
                    {
                        second = curNode;
                        break;
                    }
                }   
            }
        }
        swap(first->val, second->val);
        return;
    }
};