
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
	int countPrimes(int n) {
		if (n < 2)
		{
			return 0;

		}
		int ans = 0;
		int index;
		vector<bool> dp(n, false);
		dp[0] = true;
		dp[1] = true;
		for (int i = 2; i < n; i++)
		{
			if (dp[i] == false)
			{
				cout << i;
				ans += 1;
				index = i;
				while (index < n)
				{
					dp[index] = true;
					index += i;

				}

			}

		}


		return ans;
	}
};