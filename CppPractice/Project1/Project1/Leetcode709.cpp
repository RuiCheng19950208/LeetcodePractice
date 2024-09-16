#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
		string ans;
		for (char each: str)
		{
			if (each>='A' and each<='Z')
			{
				ans += (each + 'a' - 'A');


			}
			else
			{
				ans += each;

			}

		}
		return ans;

    }
};