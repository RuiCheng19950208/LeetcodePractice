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
    ListNode* removeElements(ListNode* head, int val) {

        ListNode* ans = new ListNode(0, head);
        ListNode* slow = ans;
        ListNode* fast = head;
        while (fast)
        {
            if (fast->val == val)
            {
                slow->next = fast->next;
                fast = fast->next;
            }
            else
            {
                fast = fast->next;
                slow = slow->next;
            }
        }
        return ans->next;
    }
};