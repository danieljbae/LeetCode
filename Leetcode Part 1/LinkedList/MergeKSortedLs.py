# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Brute force LOL!!!!
        
        
        hash_map = collections.defaultdict(list)
        
        for node in lists: 
            while node: # traverse each linkedlist 
                hash_map[node.val].append(node)  # add every node of same value to hash
                node = node.next
            
        unsorted_map = hash_map.items()
        sorted_map = sorted(unsorted_map, key = lambda x : unsorted_map[0])
        print(sorted_map)
        
            
                
                
                    
                    
                
        