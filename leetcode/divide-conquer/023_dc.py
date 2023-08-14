from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists == [[]]: return None
        if len(lists) == 1: return lists[0]

        def combine(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if l1 is None and l2 is None: return None
            if l2 is None: return l1
            if l1 is None: return l2
            out = ListNode()
            p1, p2 = l1, l2
            # initialize value of head
            if p1.val < p2.val:
                out.val = p1.val
                p1 = p1.next
            else:
                out.val = p2.val
                p2 = p2.next
            crt = out
            # start merging
            while p1 is not None and p2 is not None:
                if crt.next is None: crt.next = ListNode()
                crt = crt.next
                if p1.val < p2.val:
                    crt.val = p1.val
                    p1 = p1.next
                else:
                    crt.val = p2.val
                    p2 = p2.next
            # add what's left
            if p1 is None and p2 is None: return out
            crt.next = p2 if p1 is None else p1
            return out

        def rec(p: int, q: int) -> Optional[ListNode]:
            if p >= q: return lists[p]
            m = (p + q) // 2
            return combine(rec(p, m), rec(m + 1, q))

        return rec(0, len(lists)-1)
