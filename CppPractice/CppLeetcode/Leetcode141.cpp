class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        ListNode *fast=head;
        ListNode *slow=head;
        while(fast)
        {
            slow=slow->next;
            fast=fast->next;
            if(!fast){return false;}
            else{fast=fast->next;}
            if(slow==fast){return true;}
        }
        return false;
    }
};