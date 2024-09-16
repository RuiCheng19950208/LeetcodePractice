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


//class Solution {
//public:
//    ListNode* reverseList(ListNode* head) {
//        ListNode* ans = new ListNode();
//        ListNode* cur1 = head1;
//        ListNode* cur2 = head2;
//        int carry = 0;
//        while (cur1 or cur2 or carry==1)
//        {
//           
//            ans->val = (carry + cur1->val + cur2->val)%10;
//            carry = (carry + cur1->val + cur2->val) / 10;
//            if (cur1)
//            {
//                cur1 = cur1->next;
//
//            }
//            if (cur2)
//            {
//                cur2 = cur2->next;
//            }
//            ans->next = new ListNode();
//            ans = ans->next;
//        }
//
//        return ans;
//
//
//    }
//};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
       ListNode* ans = new ListNode();
       ListNode* cur = head;
       vector<int> val_list;
       if (!head)
       {
           return head;

       }
       while (cur!=NULL)
       {
           val_list.push_back(cur->val);
           cur = cur->next;
       }
       reverse(val_list.begin(), val_list.end());
       cur = ans;
       for (int i = 0; i < val_list.size(); i++)
       {
           cur->next = new ListNode(val_list[i]);
           cur = cur->next;

       }
       return ans->next;

    }
};


