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
	int strStr(string haystack, string needle) {
		if (needle.size() == 0)
		{
			return 0;
		}
		if (needle.size() > haystack.size())
		{
			return -1;
		}
		int ans = 0;

		for (int i = 0; i < haystack.size() - needle.size() + 1; i++)
		{
			for (int j = 0; j < needle.size(); j++)
			{

				if (haystack[i + j] != needle[j])
				{

					break;

				}
				if (j == needle.size() - 1)
				{
					return ans;
				}
			}
			ans++;

		}
		return -1;

	}
};