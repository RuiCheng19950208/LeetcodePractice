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
    bool isPerfectSquare(int num) {
		for (int i =1; i <= num/i; i++)
		{
			if (i*i==num)
			{
				return true;
			}

		}
		return false;

    }
};