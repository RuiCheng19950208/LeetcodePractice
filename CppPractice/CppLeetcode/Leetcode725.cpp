#include<vector>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode():val(0),next(nullptr){};
    ListNode(int x):val(x),next(nullptr){};
    ListNode(int x, ListNode *p):val(x),next(p){};

};

class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) 
    {
        ListNode *cur = head;
        int listLength = 0;
        while (cur)
        {
            cur=cur->next;
            listLength ++;
        }
        int averageLenth = listLength/k;
        int remainder = listLength%k;
        vector<ListNode*> ans;
        cur = head;
        for (int i = 0; i < k; i++)
        {
            ListNode *partHead = cur;
            int partLenth = averageLenth+(i<remainder?1:0);
            for (int j = 0; j < partLenth-1; j++)
            {
                cur = cur->next;
                
            }
            if (cur)
            {
                ListNode *nextHead = cur->next;
                cur->next = nullptr;
                cur = nextHead;
            }
            ans.push_back(partHead);
            
        }
        return ans;
    }
};