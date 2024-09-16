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


class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        map<Node*, Node*> ans_map;
        Node* cur = head;
        while (cur)
        {
            ans_map[cur] = new Node(cur->val);
            cur = cur->next;

        }
        cur = head;
        while (cur)
        {
            ans_map[cur]->next = ans_map[cur->next];
            ans_map[cur]->random = ans_map[cur->random];
            cur = cur->next;

        }
        return ans_map[head];

    }
};