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
        # Iterative approach - O(n) time and O(1) space
        
        cursor = head
        prev = None # intialized as null to end linked list 
        
        while cursor != None:
            next_temp = cursor.next # Swap: store value/node of the next node in sequence
            cursor.next = prev # Swap: reversing pointers 
    
            prev = cursor # Incrument: prev pointer
            cursor = next_temp # Incrument: current pointer
        
        return prev # return 