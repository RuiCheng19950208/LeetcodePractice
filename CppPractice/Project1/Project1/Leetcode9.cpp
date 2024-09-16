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
    bool isPalindrome(int x) {
		vector<int> x_list;
		if (x<0)
		{
			return false;
		}
		while (x != 0)
		{
			x_list.push_back(x % 10);
			x = x / 10;

		}
		for (int i = 0; i < x_list.size()/2; i++)
		{
			if (x_list[i]!=x_list[x_list.size()-1-i])
			{
				return false;

			}

		}
		return true;


    }
};


