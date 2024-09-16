#include<vector>
#include<algorithm>

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

class Solution {
private:
    void Traversal(TreeNode *p,vector<int> &res)
    {
        if (!p)
        {
            return;
        }
        else
        {
            Traversal(p->left,res);
            res.push_back(p->val);
            Traversal(p->right,res);
        }
    }
public:
    int kthSmallest(TreeNode* root, int k) 
    {
        vector<int> result;
        sort(result.begin(),result.end());
        return result[k-1];
        
    }
};