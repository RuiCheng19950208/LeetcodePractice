#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}

    
};

// Function to add two numbers represented by linked lists
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);  // Dummy node to simplify edge cases
    ListNode* current = &dummy;  // Pointer to build the result list
    int carry = 0;  // Carry for addition
    
    while (l1 != nullptr || l2 != nullptr || carry != 0) {
        int sum = carry;  // Start with carry from previous iteration
        
        if (l1 != nullptr) {
            sum += l1->val;  // Add value from l1
            l1 = l1->next;  // Move to next node in l1
        }
        
        if (l2 != nullptr) {
            sum += l2->val;  // Add value from l2
            l2 = l2->next;  // Move to next node in l2
        }
        
        carry = sum / 10;  // Update carry
        current->next = new ListNode(sum % 10);  // Create a new node with the current digit
        current = current->next;  // Move to the next node in the result list
    }
    
    return dummy.next;  // Return the next node after the dummy node
}

// Function to print the linked list
void printList(ListNode* head) {
    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

// Function to create a linked list from a vector
ListNode* createList(const vector<int>& values) {
    ListNode dummy(0);
    ListNode* current = &dummy;
    for (int value : values) {
        current->next = new ListNode(value);
        current = current->next;
    }
    return dummy.next;
}

int main() {
    // Create linked lists from vectors
    ListNode* l1 = createList({2, 4, 3});  // Represents 342
    ListNode* l2 = createList({5, 6, 4});  // Represents 465
    
    // Add the two numbers
    ListNode* result = addTwoNumbers(l1, l2);
    
    // Print the result
    printList(result);  // Should print 7 0 8 (represents 807)
    
    return 0;
}