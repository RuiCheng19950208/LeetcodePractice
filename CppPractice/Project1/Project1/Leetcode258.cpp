#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

using namespace std;


class Solution {
public:
    int addDigits(int num) {
        int n;
        int remain;
        int temp_sum;
        while (num>=10)
        {
            n = num;
            temp_sum = 0;
            while (n>=10)
            {
                temp_sum += n % 10;
                n = n / 10;

            }
            temp_sum += n;
            num = temp_sum;
           

        }
        return num;
    }
};