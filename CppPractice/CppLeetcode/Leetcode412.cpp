using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {

        string FizzStr ="Fizz";
        string BuzzStr= "Buzz";
        bool isFizz = false;
        bool isBuzz = false;
        vector<string> ans;

        for(int i=1;i<=n;i++)
        {
            isFizz = false;
            isBuzz = false;
            string tempStr = to_string(i);
            if (i%3==0)
            {
                isFizz = true;
            }
            if (i%5==0)
            {
                isBuzz = true;
            }
            if (isFizz && isBuzz)
            {
                tempStr = FizzStr+BuzzStr;
            }
            else if (isFizz)
            {
                tempStr=FizzStr;
            }
            else if (isBuzz)
            {
                tempStr=BuzzStr;
            }
            ans.push_back(tempStr);
        }

        return ans;
    }
};