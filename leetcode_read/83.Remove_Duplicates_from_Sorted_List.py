# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        node = head
        while node:
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head

        """
        :type head: ListNode
        :rtype: ListNode
        """