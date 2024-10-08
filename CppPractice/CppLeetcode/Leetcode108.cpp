class Solution {
public:
    vector<int> numsPublic;
    TreeNode* helper(int left,int right)
    {
        // cout<<left<<" "<<right<<endl;
        if(left>right){return nullptr;}
        int mid =left+(right-left)/2;
        TreeNode *newNode = new TreeNode(numsPublic[mid]);
        newNode->left = helper(left,mid-1);
        newNode->right = helper(mid+1,right);
        return newNode;

    }
    TreeNode* sortedArrayToBST(vector<int>& nums) 
    {
        numsPublic = nums;
        return helper(0,nums.size()-1);
    }
};