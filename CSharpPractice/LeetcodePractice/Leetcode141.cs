public class Solution141 {
    public bool HasCycle(ListNode head) 
    {
        HashSet<ListNode> visited = new HashSet<ListNode>();
        while(head!=null)
        {
            if(visited.Contains(head))
            {
                return true;
            }
            visited.Add(head);
            head =head.next;
        }
        return false;
    }
}