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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        vector<int> val_list;
        int list_index = 1;
        ListNode* cur = head;
        while (cur)
        {
            if (list_index>=left and list_index<=right)
            {
                val_list.push_back(cur->val);
            }
            list_index++;
            cur = cur->next;
        }
        reverse(val_list.begin(),val_list.end());
        cur = head;
        list_index = 1;
        while (cur)
        {
            if (list_index >= left and list_index <= right)
            {
                cur->val=val_list[list_index-left];
            }
            list_index++;
            cur = cur->next;

        }
        return head;

    }
};