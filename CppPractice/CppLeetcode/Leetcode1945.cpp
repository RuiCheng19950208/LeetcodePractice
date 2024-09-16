#include<vector>
#include<string>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode():val(0),next(nullptr){};
    ListNode(int x):val(x),next(nullptr){};
    ListNode(int x, ListNode *p):val(x),next(p){};

};

class Solution {
public:
    int getLucky(string s, int k) 
    {
        string convertedString = "";
        for(char c:s)
        {
            convertedString = convertedString + stoi(c);
        }

        int theSum = 0;
        while (k>0)
        {
            for (char c:convertedString)
            {
                theSum += stoi(c);
            }
            convertedString = to_string(theSum);
            
            k--;
        }
        return stoi(convertedString);
    }
};