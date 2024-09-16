#include "LeetcodeHeader.h"

class Solution {
public:
	vector<int> getRow(int rowIndex) {
		vector<vector<int>> triangle;
		vector<int> temp;
		if (rowIndex == 0)
		{
			return { 1 };

		}
		else if (rowIndex == 1)
		{
			return { 1,1 };
		}

		else
		{
			temp = { 1,1 };
			triangle.push_back(temp);
			for (int i = 2; i <= rowIndex; i++)
			{
				temp = {};
				for (int j = 0; j <= i; j++)
				{
					if (j == 0 or j == i)
					{
						temp.push_back(1);
					}
					else
					{
						temp.push_back(triangle.back()[j - 1] + triangle.back()[j]);
					}
				}
				triangle.push_back(temp);
			}

			return temp;
		}

	}
};