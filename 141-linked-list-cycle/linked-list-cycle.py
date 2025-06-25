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
        seen = []
        while head:
            if head not in seen:
                seen.append(head)
                head = head.next
            else:
                return True
        return False