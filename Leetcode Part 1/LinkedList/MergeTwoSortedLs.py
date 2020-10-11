# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode() # head of a new list
        cursor = head
        
        while l1 and l2:
            if (l1 and l2) and (l1.val <= l2.val): 
                cursor.next = l1 # add l1 to our new merged list 
                l1 = l1.next # incrument l1 pointer
            elif (l1 and l2) and (l1.val > l2.val): 
                cursor.next = l2 # add l2 to our new merged list 
                l2 = l2.next # incrument l2 pointer
            
            cursor = cursor.next # incrumemt merged list pointer
        
        # glue remaining nodes of whichever list is remaining to merged list
        cursor.next = l1 or l2
        
        return head.next # head of merged list
        
            
        
            
                