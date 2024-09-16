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
        ListNode *dummy = new ListNode();
        ListNode *curP = dummy;
        int carry = 0;

        while(l1 || l2)
        {
            int l1Num = l1?l1->val:0;
            int l2Num = l2?l2->val:0;
            int curSum = l1Num+l2Num+carry;
            carry = (curSum)/10;
            curP->next = new ListNode(curSum%10);
            if (l1)
            {
               l1 = l1->next;
            }
            if (l2) 
            {
                l2 = l2->next;
            }
            curP = curP->next;
            
        } 

        if (carry == 1)
        {
                 curP->next = new ListNode(1);
        }
        
        return dummy->next;

        
    }
};