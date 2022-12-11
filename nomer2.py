class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkList:
    def __init__(self):
        self.head=None
def initList(self, data):
        # Creat head node
        self.head = ListNode(data[0])
        r=self.head
        p = self.head
        # Create node for every data
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
def printlist(self,head):
        if head == None: return
        node = head
        while node != None:
            #print(node.val,end=' ')
            node = node.next