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


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int ans = nums.size();
        int pointer=0;
        int temp;
        map<int, int> record;
        while (pointer< ans)
        {
            if (record[nums[pointer]]>0)
            {
                temp = nums[pointer];
                nums[pointer] = nums[ans - 1];
                nums[ans - 1] = temp;
                ans--;
            }
            else
            {
                record[nums[pointer]]++;
                pointer++;
            }

        }

        return ans;

    }
};