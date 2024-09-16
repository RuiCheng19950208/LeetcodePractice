public class Solution24 {
    public ListNode SwapPairs(ListNode head) 
    {
        if (head==null)
        {
            return null;
        }
        else
        {
            if (head.next==null)
            {
                return head;
            }
        }
        ListNode slow = head;
        ListNode fast = slow.next;
        while (slow!=null)
        {
            if (fast!=null)
            {
                int temp = 0;
                temp=slow.val;
                slow.val = fast.val;
                fast.val=temp;
                slow = fast.next;
                if (slow!=null)
                {
                    fast = slow.next;
                }
                else
                {
                    break;
                }
            }
            else
            {
                break;
            }
        }
        return head;
    }
}