# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        tmp = head
        slow = head 
        fast2 = head.next.next 
        
        while fast2 and fast2.next:
            if not fast2.next: 
                slow.next = slow.next.next
                
            else:
                slow = slow.next
                fast2 = fast2.next
                
                
        return head
                
            
            
            
            
            
        