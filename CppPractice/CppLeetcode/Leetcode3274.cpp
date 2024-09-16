#include<string>
using namespace std;

class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) 
    {
        int sumCoor1 = (coordinate1[0]-'a'+1)+(coordinate1[1]-'0');
        int sumCoor2 = (coordinate2[0]-'a'+1)+(coordinate2[1]-'0');
        return(sumCoor1%2==sumCoor2%2);
        
    }
};