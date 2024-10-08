#include <vector>
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        for(int i = 1; i < n+1; i++)
        {
            ans.push_back(i);
        }
        // Sort the vector in ascending order
        sort(ans.begin(), ans.end(),[](int a,int b){
            return to_string(a)<to_string(b);
        });

        return ans;
    }
};