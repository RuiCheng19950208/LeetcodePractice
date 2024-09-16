var swapPairs = function(head) {
    if (head==null) 
    {
        return null;   
    }
    else if (head.next ==null) {
        return head;
    }
    let slow = head
    let fast = head.next
    while (slow) {
        if (fast) {
            let t = slow.val;
            slow.val = fast.val;
            fast.val = t;
            slow = fast.next
            if (slow) {
                fast = slow.next
                
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
    
};