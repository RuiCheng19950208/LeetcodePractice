#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;


struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
    
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode();
        ListNode* cur = head;
        ListNode* cur_1 = l1;
        ListNode* cur_2 = l2;
        if (!l1)
        {
            return l2;

        }
        if (!l2)
        {
            return l1;

        }
        while (cur_1!=NULL or cur_2!=NULL)
        {
            if (cur_1 != NULL and cur_2 != NULL)
            {
                if (cur_1->val < cur_2->val)
                {
                    cur->next = new ListNode(cur_1->val);
                    cur = cur->next;
                    cur_1 = cur_1->next;


                }
                else
                {
                    cur->next = new ListNode(cur_2->val);
                    cur = cur->next;
                    cur_2 = cur_2->next;

                }

            }
            else if (cur_1 != NULL)
            {
                cur->next = new ListNode(cur_1->val);
                cur = cur->next;
                cur_1 = cur_1->next;


            }
            else
            {

                cur->next = new ListNode(cur_2->val);
                cur = cur->next;
                cur_2 = cur_2->next;

            }
        }

        return head->next;

        

    }
};