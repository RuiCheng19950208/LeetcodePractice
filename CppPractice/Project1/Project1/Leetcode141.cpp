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
    bool hasCycle(ListNode* head) {
        ListNode* cur = head;
        vector<ListNode*> exist;
        while (cur)
        {
            if (find(exist.begin(), exist.end(), cur) == exist.end())
            {
                exist.push_back(cur);
            }
            else
            {
                return true;
            }
            cur = cur->next;


        }

        return false;
    }
};