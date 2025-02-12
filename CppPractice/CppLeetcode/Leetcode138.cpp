
// Definition for a Node.
// class Node {
// public:
//     int val;
//     Node* next;
//     Node* random;
    
//     Node(int _val) {
//         val = _val;
//         next = NULL;
//         random = NULL;
//     }
// };


class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> theMap;
        Node* cur = head;
        while(cur)
        {
            theMap[cur] = new Node(cur->val);
            cur = cur->next;
        }
        cur =head;
        while(cur)
        {
            theMap[cur]->next = theMap[cur->next];
            theMap[cur]->random = theMap[cur->random];
            cur=cur->next;
        }
        return theMap[head];
    }
};