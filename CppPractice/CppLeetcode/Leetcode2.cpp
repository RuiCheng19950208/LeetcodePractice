#include<vector>


struct ListNode
{
    int val;
    ListNode *next;
    ListNode(): val(0),next(nullptr){};
    ListNode(int x): val(x) ,next(nullptr){};
    ListNode(int x, ListNode *p): val(x), next(p){};
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        int carry=0;
        ListNode *root= new ListNode();
        ListNode *cur = root;
        ListNode *cur1=l1;
        ListNode *cur2=l2;
        while(cur1||cur2||carry)
        {
            int digit1=0;
            int digit2=0;
            if(cur1)
            {
                digit1 = cur1->val;
                cur1 = cur1->next;
            }
            if(cur2)
            {
                digit2 = cur2->val;
                cur2 = cur2->next;
            }
            cur->next = new ListNode((digit1+digit2+carry)%10);
            cur =cur->next;
            carry = (digit1+digit2+carry)/10;

        }
        return root->next;
    }
};