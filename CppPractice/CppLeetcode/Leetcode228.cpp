#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) 
    {
        vector<string> ans;
        bool isConcatenate  = false;
        int start = 0;
        int end = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (!isConcatenate)
            {
                start = nums[i];
                if (i+1<nums.size() && nums[i+1] - nums[i]==1)
                {
                    isConcatenate = true;
                }
                else
                {
                    ans.push_back(to_string(start));
                    isConcatenate = false;
                }
            }
            else
            {
                end= nums[i];
                string tempAns = to_string(start)+"->"+to_string(end);
                if (i+1<nums.size() && nums[i+1] == nums[i]+1)
                {
                    isConcatenate = true;
                }
                else
                {
                    ans.push_back(tempAns);
                    isConcatenate = false;
                }
            }
        }
        return ans;
    }
};