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
    ListNode* detectCycle(ListNode* head) {
        vector<ListNode*> record;
        ListNode* cur = head;
        while (cur)
        {
            if (find(record.begin(),record.end(),cur)!=record.end())
            {
                return cur;
            }
            record.push_back(cur);
            cur = cur->next;

        }
        return NULL;

    }
};
