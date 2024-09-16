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
    void setZeroes(vector<vector<int>>& matrix) {
		bool row_zero = false;
		bool col_zero = false;
		if (matrix.size()==1)
		{
			for (int i = 0; i < matrix[0].size(); i++)
			{
				if (matrix[0][i]==0)
				{
					for (int j = 0; j < matrix[0].size(); j++)
					{
						matrix[0][j] = 0;
					}
					break;

				}
				
			}

		}
		else if (matrix[0].size() == 1)
		{
			for (int i = 0; i < matrix.size(); i++)
			{
				if (matrix[i][0] == 0)
				{
					for (int j = 0; j < matrix.size(); j++)
					{
						matrix[j][0] = 0;
					}
					break;
				}
			}
		}
		else
		{
			for (int i = 0; i < matrix.size(); i++)
			{
				if (matrix[i][0]==0)
				{
					col_zero = true;
					break;
					
				}
			
			}
			for (int i = 0; i < matrix[0].size(); i++)
			{
				if (matrix[0][i] == 0)
				{
					row_zero = true;
					break;

				}
			}
			for (int i = 1; i < matrix.size(); i++)
			{
				for (int j = 1; j < matrix[0].size(); j++)
				{
					if (matrix[i][j]==0)
					{
						matrix[0][j] = 0;
						matrix[i][0] = 0;

					}

				}
			}
			for (int i = 1; i < matrix.size(); i++)
			{
				if (matrix[i][0]==0)
				{
					for (int j = 1; j < matrix[0].size(); j++)
					{
						matrix[i][j] = 0;

					}

				}

			}
			for (int i = 1; i < matrix[0].size(); i++)
			{
				if (matrix[0][i] == 0)
				{
					for (int j = 1; j < matrix.size(); j++)
					{
						matrix[j][i] = 0;

					}

				}

			}

			if (row_zero)
			{
				for (int i = 0; i < matrix[0].size(); i++)
				{
					matrix[0][i] = 0;

				}

			}
			if (col_zero)
			{
				for (int i = 0; i < matrix.size(); i++)
				{
					matrix[i][0] = 0;

				}

			}
		}

    }
};