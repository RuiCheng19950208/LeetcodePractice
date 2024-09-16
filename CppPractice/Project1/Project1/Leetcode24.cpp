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
    ListNode* swapPairs(ListNode* head) {
        if (!head)
        {
            return head;
        }
        ListNode* ans = head;
        ListNode* slow = head;
        ListNode* fast = head->next;
        int temp;

        if (!fast)
        {
            return head;
        }
        else
        {
            while (fast and slow)
            {
                swap(fast->val, slow->val);
                slow = slow->next->next;
                if (slow)
                {
                    fast = slow->next;
                }
            }
        }
        return ans;
    }
};