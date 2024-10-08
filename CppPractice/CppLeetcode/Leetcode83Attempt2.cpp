class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head){return nullptr;}
        vector<int> candidates;
        ListNode *ans = new ListNode();
        ListNode *cur = head;
        while(cur)
        {
            if(find(candidates.begin(),candidates.end(),cur->val)==candidates.end()){candidates.push_back(cur->val);}
            cur=cur->next;
        }
        cur=ans;
        for(int i=0; i<candidates.size();i++)
        {
            cur->next = new ListNode(candidates[i]);
            cur=cur->next;
        }


        return ans->next;
    }
};