# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middleNode = head
        end = head
        while end and end.next:
            middleNode = middleNode.next
            end = end.next.next
        return middleNode