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
    string removeKdigits(string num, int k) {
		vector<char> char_list;
		int pointer = 1;
		string ans;
		char_list.push_back(num[0]);

		while (pointer<num.size())
		{
			if (k>0 and char_list.size()>0)
			{
				if (num[pointer] < char_list.back())
				{
					char_list.pop_back();
					k--;
				}
				else
				{
					char_list.push_back(num[pointer]);
					pointer++;

				}

			}
			else
			{
				char_list.push_back(num[pointer]);
				pointer++;
			}
		}
		while (k>0)
		{
			char_list.pop_back();
			k--;
		}
		for (int i = 0; i < char_list.size(); i++)
		{
			if (ans.size()==0 and char_list[i]=='0')
			{

			}
			else
			{
				ans += char_list[i];
			}
			
		}
		if (ans.size()==0)
		{
			return "0";
		}
		else
		{
			return ans;

		}
	

    }
};

