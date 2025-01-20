class Solution {
public:
    vector<int> numList;
    void helper(TreeNode* node)
    {
        if(!node){return;}
        numList.push_back(node->val);
        helper(node->right);
        helper(node->left);
        return;
    }
    int getMinimumDifference(TreeNode* root) 
    {
        helper(root);
        int ans=100000;
        sort(numList.begin(),numList.end());
        for(int i=1;i<numList.size();i++)
        {
            if(numList[i]-numList[i-1]<ans)
            {
                ans=numList[i]-numList[i-1];
            }
        }
        return ans;
    }
};