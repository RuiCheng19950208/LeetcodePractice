#include<set>
#include<vector>
#include<utility>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(): val(0),next(nullptr){};
    ListNode(int x): val(x),next(nullptr){};
    ListNode(int x,ListNode *p): val(x),next(p){};
};

class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) 
    {
        set<int> numSet;
        for (int num:nums)
        {
            numSet.insert(num);
        }
        //Process head first
        while (numSet.find(head->val)!=numSet.end())
        {
            head = head->next;
        }
        //Process following node
        ListNode *p = head;
        while (p)
        {
            if(p->next)
            {
                if(numSet.find(p->next->val)!=numSet.end())
                {
                    p->next = p->next->next;
                }
                else
                {
                    p = p->next;
                }
            }
            else
            {
                break;
            }

        }
        return head;
    }
};