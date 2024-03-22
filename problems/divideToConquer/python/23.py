#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.


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
    
        def sort_two_linked_lists(L1, L2) :
            result = ListNode()
            curr = result

            while L1 and L2 :
                if L1.val < L2.val :
                    curr.next = L1
                    L1 = L1.next
                else :
                    curr.next = L2
                    L2 = L2.next
                curr = curr.next
            if L1 :
                curr.next = L1
            elif L2:
                curr.next = L2

            return result.next
            
        def merge_k_lists(lists):
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]

            mid = len(lists) // 2
            left = merge_k_lists(lists[:mid])
            right = merge_k_lists(lists[mid:])

            return sort_two_linked_lists(left, right)

        return merge_k_lists(lists)

# Time complexity O(n log k) with n the number of nodes in all lists and k the number of lists
# Space complexity is O(n) with n the number of nodes in all lists