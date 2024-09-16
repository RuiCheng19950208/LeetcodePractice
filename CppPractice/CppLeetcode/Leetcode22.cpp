#include<vector>
#include<string>
#include<deque>
#include<tuple>

using namespace std;


class Solution {
public:
    vector<string> generateParenthesis(int n) 
    {
        
        vector<string> res;
        deque<tuple<int,int,string>> theQueue;
        
        theQueue.push_back(make_tuple(0,0,""));

        while (theQueue.size()>0)
        {
            tuple<int,int,string> curState = theQueue.front();
            int curLeft= get<0>(curState);
            int curRight= get<1>(curState);
            string curString =get<2>(curState);
            theQueue.pop_front();
            if (curLeft==n && curRight==n)
            {
                res.push_back(curString);
                continue;
            }
            if (curLeft<n)
            {
                theQueue.push_back(make_tuple(curLeft+1,curRight,curString+"("));
            }
            if (curLeft>curRight && curRight<n)
            {
                theQueue.push_back(make_tuple(curLeft,curRight+1,curString+")"));
            }
        }
        return res;
    }
};