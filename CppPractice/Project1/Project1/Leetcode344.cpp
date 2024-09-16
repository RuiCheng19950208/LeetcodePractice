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
	void reverseString(vector<char>& s) {
		int left_pointer = s.size() - 1;
		char temp;
		for (int i = 0; i < s.size() / 2; i++)
		{
			temp = s[left_pointer];
			s[left_pointer] = s[i];
			s[i] = temp;
			left_pointer--;
		}

	}
};