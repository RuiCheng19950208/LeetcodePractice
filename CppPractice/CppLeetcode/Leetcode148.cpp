class Solution {
public:
    ListNode* sortList(ListNode* head) 
    {
        ListNode *cur = head;
        vector<int> numList;
        while(cur)
        {
            numList.push_back(cur->val);
            cur=cur->next;
        }
        sort(numList.begin(),numList.end());
        cur =head;
        int curIndex = 0;
        while(cur)
        {
            cur->val = numList[curIndex];
            cur = cur->next;
            curIndex++;
        }
        return head;
    }
};