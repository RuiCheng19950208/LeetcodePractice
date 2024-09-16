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
    ListNode* middleNode(ListNode* head) {
        int len_list = 0;
        int target_index ;
        ListNode* cur=head;
        ListNode* ans;
        while (cur)
        {
            len_list++;
            cur = cur->next;
        }
        target_index = len_list / 2;
        cur = head;
        while (target_index>0)
        {
            target_index--;
            cur = cur->next;
            ans = cur;
        }
        return ans;


    }
};
