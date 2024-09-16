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
    void reorderList(ListNode* head) {
        ListNode* cur = head;
        vector<int> val_list;
        vector<int> new_val_list;
        int begin = 0;
        int end = 0;
        while (cur!=NULL)
        {
            val_list.push_back(cur->val);
            cur = cur->next;
        }
        end = val_list.size() - 1;
        while (begin<=end)
        {
            new_val_list.push_back(val_list[begin]);
            begin++;
            if (begin<=end)
            {
                new_val_list.push_back(val_list[end]);
                end--;

            }
        }
        cur = head;
        begin = 0;
        while (cur)
        {
            cur->val = new_val_list[begin];
            cur = cur->next;
            begin ++;

        }
        return;

    }
};