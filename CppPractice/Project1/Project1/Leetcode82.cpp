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
        vector<int> val_list;
        while (cur)
        {
            if (val_list.size() == 0)
            {
                val_list.push_back(cur->val);
                cur = cur->next;
            }
            else if (cur->val == val_list.back())
            {
                while (cur and cur->val == val_list.back())
                {
                    cur = cur->next;
                }
                val_list.pop_back();
            }
            else
            {
                val_list.push_back(cur->val);
                cur = cur->next;
            }
        }
        cur = ans;
        for (int i = 0; i < val_list.size(); i++)
        {
            cur->next = new ListNode(val_list[i]);
            cur = cur->next;
        }

        return ans->next;

    }
};