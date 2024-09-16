#include<vector>
#include<string>


using namespace std;

class Solution {
public:
    string temp = "";
    int publicN;
    vector<string> res;

    void helper(int left,int right,string temp)
    {
        if(left>publicN){return;}
        if (left==publicN && right==publicN)
        {
            res.push_back(temp);
            return;
        }
        if(left<publicN)
        {
            helper(left+1,right,temp+"(");
        }
        
        if (left>right)
        {
            helper(left,right+1,temp+")");
        }
    }
    vector<string> generateParenthesis(int n) 
    {
        publicN = n;
        helper(0,0,temp);
        return res;
    }

};