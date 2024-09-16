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
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        vector<ListNode*> A;
        vector<ListNode*> B;
        ListNode* curA = headA;
        ListNode* curB = headB;
        while (curA)
        {
            A.push_back(curA);
            curA = curA->next;

        }
        while (curB)
        {
            B.push_back(curB);
            curB = curB->next;

        }
        for (int i = 0; i < A.size(); i++)
        {
            if (find(B.begin(), B.end(), A[i]) != B.end())
            {
                return A[i];

            }
        }

        return NULL;
    }
};