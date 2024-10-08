class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head){return nullptr;}
        ListNode *fast=head->next;
        ListNode *slow=head;
        while(fast)
        {
            if(slow->val==fast->val)
            {
                slow->next=fast->next;
                fast = slow->next;
            }
            else
            {
                slow=fast;
                fast=fast->next;
            }
        }
        return head;
    }
};