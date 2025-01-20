public class Solution83 {
    public ListNode DeleteDuplicates(ListNode head) 
    {
        if(head ==null){return null;}
        ListNode fast =head;
        ListNode slow =head;
        while(fast!=null)
        {
            
            if(slow.val!=fast.val)
            {
                slow.next = fast;
                slow = slow.next;

            }
            fast =fast.next;
        }
        slow.next =null;
        return head;
    }
}