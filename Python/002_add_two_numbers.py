class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    carry = 0
    head = current =ListNode(0)
    def addTwoNumbers(self,m,n):
        while m or n:
                val = carry
                if m:
                    val += m.val
                    m = m.next
                if n:
                    val += n.val
                    n=n.next
                current.next = ListNode(val%10)
                current = current.next
                carry = val/10
        if carry > 0:
            current.next = ListNode(carry)
        return head.next