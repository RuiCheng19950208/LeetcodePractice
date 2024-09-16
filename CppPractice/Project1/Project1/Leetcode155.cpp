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

class MinStack {
public:
    /** initialize your data structure here. */
    vector<int> stack;
    MinStack() {
        MinStack::stack = stack;
    }

    void push(int val) {
        MinStack::stack.push_back(val);
    }

    void pop() {
        MinStack::stack.pop_back();
    }

    int top() {
        return MinStack::stack[MinStack::stack.size()-1];

    }

    int getMin() {
        int min_val = INT_MAX;
        for ( int i = 0; i < MinStack::stack.size(); i++)
        {
            if (min_val>MinStack::stack[i])
            {
                min_val = MinStack::stack[i];
            }
        }
        return min_val;
    }
};

