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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode();
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        ListNode* cur_ans = ans;
        int res1 = 0;
        int res2 = 0;
        int carry = 0;
        int temp = 0;
        while (cur1 or cur2 or carry > 0)
        {
            if (!cur1 and cur2)
            {
                temp = cur2->val + carry;
                carry = temp / 10;
                cur_ans->next = new ListNode(temp % 10);
                cur_ans = cur_ans->next;
                cur2 = cur2->next;

            }
            else if (!cur2 and cur1)
            {
                temp = cur1->val + carry;
                carry = temp / 10;
                cur_ans->next = new ListNode(temp % 10);
                cur_ans = cur_ans->next;
                cur1 = cur1->next;


            }
            else if (!cur1 and !cur2 and carry == 1)
            {
                carry = 0;
                cur_ans->next = new ListNode(1);
                cur_ans = cur_ans->next;

            }
            else
            {
                temp = cur1->val + cur2->val + carry;
                carry = temp / 10;
                cur_ans->next = new ListNode(temp % 10);
                cur_ans = cur_ans->next;
                cur1 = cur1->next;
                cur2 = cur2->next;


            }
        }

        return ans->next;
    }
};