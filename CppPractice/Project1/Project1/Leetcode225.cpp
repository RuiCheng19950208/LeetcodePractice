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

class MyStack {
public:
    /** Initialize your data structure here. */
    vector<int> mystack;
    MyStack() {

    }

    /** Push element x onto stack. */
    void push(int x) {
        mystack.push_back(x);

    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int ans = mystack.back();
        mystack.pop_back();
        return ans;

    }

    /** Get the top element. */
    int top() {
        return mystack.back();

    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return mystack.size() == 0;

    }
};