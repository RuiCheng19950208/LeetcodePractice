#include<vector>
#include<iostream>
#include <queue>
#include <deque>
#include <string>
#include <set>
#include <tuple>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode():val(0),right(nullptr),left(nullptr){}
    TreeNode(int x): val(x),left(nullptr),right(nullptr){}
    TreeNode(int x, TreeNode *Right, TreeNode *Left): val(x),left(Left),right(Right){}

};


class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) 
    {
        vector<string> ans;
        if(!root){return ans;}
        deque<pair<TreeNode*,string>> theQueue;
        theQueue.push_back({root,to_string(root->val)});


        while (!theQueue.empty())
        {
            TreeNode *curNode =theQueue.front().first;
            string curPath = theQueue.front().second;
            theQueue.pop_front();

            if (!curNode->left && !curNode->right)
            {
                ans.push_back(curPath);
            }
            if (curNode->left)
            {
                theQueue.push_back({curNode->left,curPath+"->"+to_string(curNode->left->val)});
            }
            if (curNode->right)
            {
                theQueue.push_back({curNode->right,curPath+"->" + to_string(curNode->right->val)});
            }
            

        }
        return ans;

        
    }
};

