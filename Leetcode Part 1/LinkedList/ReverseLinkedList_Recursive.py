# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursive approach - O(n) time and O(n) space
        
        if (not head) or (not head.next): # end of linked list
            return head
        
        rev_head = self.reverseList(head.next) # recurse - downwards on stack  
        head.next.next = head # reversal - logic: next node will now point to current node
        head.next = None # remove existing link, such that linkedlist remains singly linked
        return rev_head # return recursion - upwards stack 