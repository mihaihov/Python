class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

def initializeLinkedList(n) -> ListNode:
    if n == 0:
        return ListNode(0)

    dummyStart = ListNode()
    start = dummyStart

    while n != 0:
        start.next = ListNode(n%10)
        n = int(n/10)
        start = start.next
    return dummyStart.next

def printLinkedList(start : ListNode):
    while(start != None):
        print(start.val,end=" ")
        start = start.next


def getLinkedListLength(number: ListNode) -> int:
    len : int = 0
    while(number != None):
        len += 1
        number = number.next
    
    return len

def addLinkedListNumbers(n: ListNode, m: ListNode) -> ListNode:
    startDummy : ListNode = ListNode()
    start = startDummy
    
    carry : int = 0
    while n or m or carry:
        nDigit = n.val if n else 0
        mDigit = m.val if m else 0
        
        sum = nDigit + mDigit + carry
        carry = sum // 10

        start.next = ListNode(sum%10)
        start = start.next

        if n:
            n = n.next
        if m:
            m = m.next
    
    return startDummy.next





    # nLen = getLinkedListLength(n)
    # mLen = getLinkedListLength(m)

    # hold : int = 0

    # dummyStart = ListNode()
    # start = dummyStart

    # if nLen > mLen:
    #     while n != None:
    #         nDigit : int = n.val
    #         mDigit : int  = 0
    #         if m != None:
    #             mDigit = m.val

    #         digitSum = nDigit + mDigit + hold
    #         hold = int(digitSum / 10)

    #         start.next = ListNode(digitSum%10)
    #         start = start.next
    #         n = n.next
    #         if m != None:
    #             if m.next != None:
    #                 m = m.next
    #             else:
    #                 m = None
    #     if hold != 0:
    #         start.next = ListNode(hold)
    #         start = start.next
    # else:942
    #     while m != None:
    #         mDigit : int = m.val
    #         nDigit : int  = 0
    #         if n != None:
    #             nDigit = n.val

    #         digitSum = nDigit + mDigit + hold
    #         hold = int(digitSum / 10)

    #         start.next = ListNode(digitSum%10)
    #         start = start.next
    #         m = m.next
    #         if n != None:
    #             if n.next != None:
    #                 n = n.next
    #             else:
    #                 n = None
    #     if hold != 0:
    #         start.next = ListNode(hold)
    #         start = start.next
    # return dummyStart.next
        


n = int(input("n: "))
m = int(input("m: "))
firstNumber = initializeLinkedList(n)
secondNumber = initializeLinkedList(m)
sum = addLinkedListNumbers(firstNumber,secondNumber)
printLinkedList(sum)