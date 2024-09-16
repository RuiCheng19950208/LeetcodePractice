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


class MyQueue {
public:
    /** Initialize your data structure here. */
    vector<int> myqueue;
    MyQueue() {

    }

    /** Push element x to the back of queue. */
    void push(int x) {
        myqueue.push_back(x);

    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int ans = myqueue[0];
        if (myqueue.size() > 0)
        {

            for (int i = 1; i < myqueue.size(); i++)
            {
                myqueue[i - 1] = myqueue[i];

            }
            myqueue.pop_back();
        }
        return ans;


    }

    /** Get the front element. */
    int peek() {
        return myqueue[0];

    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return myqueue.size() == 0;

    }
};