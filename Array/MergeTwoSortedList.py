from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)

        curNode = dummyHead
        while list1 and list2:
            if list1.val <= list2.val:
                curNode.next = list1
                list1 = list1.next
            else:
                curNode.next = list2
                list2 = list2.next
            curNode = curNode.next
        curNode.next = list1 if list1 is not None else list2

        return dummyHead.next

l1 = ListNode(1,None)
l2 = ListNode(2,None)
l3 = ListNode(3,None)
l1.next = l2
res = Solution().mergeTwoLists(l1,l3)
while res:
    print(res.val)
    res = res.next