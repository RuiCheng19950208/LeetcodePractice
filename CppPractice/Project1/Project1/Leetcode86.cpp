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
    ListNode* partition(ListNode* head, int x) {
        vector<int> record;
        vector<int> new_record;
        ListNode* cur = head;
        int list_ind = 0;
        while (cur)
        {
            record.push_back(cur->val);
            cur = cur->next;
        }

        for (int i = 0; i < record.size(); i++)
        {
            if (record[i]<x)
            {
                new_record.push_back(record[i]);
            }

        }
        for (int i = 0; i < record.size(); i++)
        {
            if (record[i] >= x)
            {
                new_record.push_back(record[i]);
            }

        }
        cur = head;
        while (cur)
        {
            cur->val = new_record[list_ind];
            list_ind++;
            cur = cur->next;
        }
        return head;

    }
};