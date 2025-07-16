class listNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
def addTwoNumber(l1,l2):
    dummy = listNode(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val_1 = l1.val if l1 else 0
        val_2 = l2.val if l2 else 0

        total = val_1 + val_2 + carry
        carry = total//10
        current.next = listNode(total%10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next