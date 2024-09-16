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

class MedianFinder {
public:
    /** initialize your data structure here. */
    vector<int> ans;
    MedianFinder() {

    }

    void addNum(int num) {
        ans.push_back(num);

    }

    double findMedian() {
        double res=0.0f;
        sort(ans.begin(), ans.end());
        if (ans.size()%2==1)
        {
            return (double)ans[ans.size()/2];
        }
        else
        {
            return ((double)ans[ans.size() / 2]+ (double)ans[(ans.size() / 2)-1])/2.0f;

        }

        return res;

    }
};
