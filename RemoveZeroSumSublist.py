from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ddict = {}
        prefixSum = 0
        dummy = ListNode(0)
        dummy.next = head

        temp = dummy
        while temp != None:
            prefixSum = prefixSum + temp.val
            ddict[prefixSum] = temp
            temp = temp.next
        
        prefixSum = 0
        cur = dummy
        while cur != None:
            prefixSum = prefixSum + cur.val
            if prefixSum in ddict:
                cur.next = ddict[prefixSum].next
            cur = cur.next

        return dummy.next


       


if __name__ == "__main__":
    eight = ListNode(1,None)
    seven = ListNode(-5,eight)
    six = ListNode(5,seven)
    five = ListNode(5,six)
    four = ListNode(-3,five)
    three = ListNode(2,four)
    two = ListNode(3,three)
    head = ListNode(1,two)
    print(Solution().removeZeroSumSublists(head))
    # [1,3,2,-3,-2,5,5,-5,1]