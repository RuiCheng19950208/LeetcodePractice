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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> num1;
        vector<int> num2;
        vector<int> num_sum;
        int ans1 = 0;
        int ans2 = 0;
        int carry = 0;
        int num_ind = 0;
        int temp = 0;
        ListNode* ans = new ListNode();
        ListNode* res = ans;
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        while (cur1)
        {
            num1.push_back(cur1->val);
            cur1 = cur1->next;
        }
        while (cur2)
        {
            num2.push_back(cur2->val);
            cur2 = cur2->next;
        }
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        while (num_ind < max(num1.size(), num2.size()) or carry == 1)
        {
            temp += carry;
            if (num_ind < num1.size())
            {
                temp += num1[num_ind];

            }
            if (num_ind < num2.size())
            {
                temp += num2[num_ind];

            }
            carry = temp / 10;
            temp = temp % 10;
            num_sum.push_back(temp);
            temp = 0;
            num_ind++;
        }


        while (num_sum.size() > 0)
        {
            ans->next = new ListNode(num_sum.back());
            num_sum.pop_back();
            ans = ans->next;
        }
        if (res->next)
        {
            return res->next;

        }
        else
        {
            return new ListNode(0);
        }



    }
};