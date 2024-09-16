#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;


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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p==NULL and q==NULL)
        {
            return true;


        }
        else if (p==NULL or q==NULL)
        {
            return false;
        }
        else if (p->val==q->val)
        {
           return(isSameTree(p->right, q->right) and isSameTree(p->left, q->left));;

        }
        else
        {
            return false;
        }


       
    }
};