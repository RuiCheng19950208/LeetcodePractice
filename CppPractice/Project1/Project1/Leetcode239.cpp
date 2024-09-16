#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

#include <set>

#include <deque>


using namespace std;



class MonotonicQueue {
public:
    void pop(){
        data.pop_front();
    
    }
    void push(int val) {
        while (!data.empty() and val>data.back())
        {
            data.pop_back();
        }
        data.push_back(val);
    }
    int max() const {
        return data.front();
    }
private:
    deque<int> data;
};


class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        MonotonicQueue myqueue;
        for (int i = 0; i < nums.size(); i++)
        {
            myqueue.push(nums[i]);
            if (i>=k-1)
            {
                ans.push_back(myqueue.max());
                if (nums[i - k + 1] == myqueue.max())
                {
                    myqueue.pop();
                }
            }

            
        }
        return ans;
       
       
    }
};

// Brute force not OK
//class Solution {
//public:
//    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
//        vector<int> ans;
//        int left = 0;
//        int right = k - 1;
//        for (int i = 0; i < nums.size()-k; i++)
//        {
//
//            ans.push_back(*max_element(nums.begin()+left,nums.begin()+right+1));
//            left++;
//            right++;
//        }
//
//        return ans;
//
//    }
//};