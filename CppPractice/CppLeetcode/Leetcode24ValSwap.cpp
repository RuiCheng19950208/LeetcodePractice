class Solution {
public:
    void swapVal(int &a,int &b)
    {
        int t = a;
        a = b;
        b = t;
    }
    ListNode* swapPairs(ListNode* head) 
    {
        if(!head)
        {
            return nullptr;
        }
        if(!head->next)
        {
            return head;
        }
        ListNode *slow = head;
        ListNode *fast = head->next; 
        while (slow)
        {
            swapVal(slow->val,fast->val)
            slow = fast->next;
            if(slow)
            {
                fast = slow->next;
            }
            else
            {
                break;
            }
            
        }
        return head;
        
    }
};