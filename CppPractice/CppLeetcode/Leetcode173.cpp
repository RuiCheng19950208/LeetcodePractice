#include<vector>
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

class BSTIterator {
private:
    vector<TreeNode*> theList;
    void PushLeft(TreeNode *p)
    {
        if (p)
        {
            theList.push_back(p);
            PushLeft(p->left);
        }
        return;
    }
public:
    BSTIterator(TreeNode* root) {
        PushLeft(root);
        
    }
    
    int next() 
    {
        TreeNode *nextP = theList.back();
        theList.pop_back();
        PushLeft(nextP->right);
        return nextP->val;
        
    }
    
    bool hasNext() 
    {
        return (theList.size()>0);
        
    }
};
