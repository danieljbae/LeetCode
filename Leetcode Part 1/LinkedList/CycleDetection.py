# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        slow = head.next
        fast = head.next.next
        
        while slow != fast:
            if (not fast) or (not fast.next): # if slow or fast is null, then no cycle
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
                
        
        
        