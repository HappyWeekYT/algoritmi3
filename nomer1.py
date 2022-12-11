class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        stak = []
        while fast and fast.next:
            stak.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            top = stak.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True