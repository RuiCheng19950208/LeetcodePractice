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
	double myPow(double x, int n) {

		if (n==0)
		{
			return 1;
		}

		double val = myPow(x, n / 2);
        		if (n<0)
		{
			x = 1 / x;
		}

		if (abs(n)%2==1)
		{
			return val * val * x;
		}
		else
		{
			return val * val;

		}
	}
};