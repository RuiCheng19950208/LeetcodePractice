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
    bool isPalindrome(ListNode* head) {
        vector<int> val_list;
        ListNode* cur = head;
        int end_index;
        int begin_index=0;
        while (cur)
        {
            val_list.push_back(cur->val);
            cur = cur->next;

        }
        end_index = val_list.size() - 1;
        while (begin_index<end_index)
        {
            if (val_list[begin_index]!=val_list[end_index])
            {
                return false;
            }
            begin_index++;
            end_index--;
        }
        return true;
    }
};