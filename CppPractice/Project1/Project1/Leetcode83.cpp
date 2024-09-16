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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* ans = new ListNode();
        ListNode* cur = head;
        ListNode* cur_ans = ans;
        vector<int> appear;
        while (cur != NULL)
        {
            if (find(appear.begin(), appear.end(), cur->val) == appear.end())
            {
                appear.push_back(cur->val);
                cur_ans->next = new ListNode(cur->val);
                cur_ans = cur_ans->next;

            }
            cur = cur->next;

        }
        return ans->next;

    }
};