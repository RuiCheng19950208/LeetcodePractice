public class Solution412 {
    public IList<string> FizzBuzz(int n) {
        IList<string> ans = new List<string>();
        bool isBuzz=false;
        bool isFizz=false;
        for (var i = 1; i < n+1; i++)
        {
            isBuzz=false;
            isFizz=false;
            string temp=i.ToString();
            if (i%3==0)
            {
                isFizz = true;
            }
            if (i%5==0)
            {
                isBuzz=true;
            }
            if (isFizz && isBuzz)
            {
                temp="FizzBuzz";
            }
            else if (isFizz)
            {
                temp="Fizz";
            }
            else if (isBuzz)
            {
                temp="Buzz";
            }
            ans.Add(temp);
        }

        return ans;
    }
}