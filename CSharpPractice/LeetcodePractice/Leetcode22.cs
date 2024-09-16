using System.Security.Cryptography.X509Certificates;

public class Solution22 {
    public IList<string> GenerateParenthesis(int n) 
    {
        IList<string> result = new List<string>();
        Dictionary<string,int> LeftRightDict = new Dictionary<string, int>{{"R",0},{"L",0}};
        Tuple<int,int,string> curState = new Tuple<int, int,string>(0,0,"");
        LinkedList<Tuple<int,int,string>> theQueue = new LinkedList<Tuple<int, int,string>>();
        theQueue.AddLast(curState);
        while (theQueue.Count>0)
        {
            curState = theQueue.Last.Value;
            theQueue.RemoveLast();
            if(curState.Item1 + curState.Item2==2*n)
            {
                result.Add(curState.Item3);
            }
            if(curState.Item1<n && curState.Item1>=curState.Item2)
            {
                theQueue.AddLast(new Tuple<int,int,string>(curState.Item1+1,curState.Item2,curState.Item3+"("));
            }
            if(curState.Item2<n && curState.Item1>curState.Item2)
            {
                theQueue.AddLast(new Tuple<int,int,string>(curState.Item1,curState.Item2+1,curState.Item3+")"));
            }   
        }
        return result;
    }
}