# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self, l):
        while(l != None):
            print(l.val)
            l = l.next

    def addItem(self, g, n):
        if g == None:
            return n

        l = g
        while(l.next != None):
            l = l.next
        
        l.next = n
        return g

class Solution:
    def mergeTwoLists(self, l1, l2):

        if(l1 == None):
            return l2
        
        if(l2 == None):
            return l1

        if(l1.val > l2.val):
            newNode = ListNode(l2.val)
            newNode.next = l1
            l1 = newNode
            l2 = l2.next

        
        n = l1
        l = l1.next
        while(l != None and l2 != None):
            if(l.val >= l2.val):
                newNode = ListNode(l2.val)
                newNode.next = l
                n.next = newNode
                l2 = l2.next
                l = newNode
            
            l = l.next
            n = n.next
        
        if l == None:
            n.next = l2

        return l1

key = ListNode(1)
g = ListNode(2)
h = ListNode(4)
key = key.addItem(key, g)
key = key.addItem(key, h)

key1 = ListNode(1)
g = ListNode(3)
h = ListNode(4)
key1 = key1.addItem(key1, g)
key1 = key1.addItem(key1, h)

new = Solution()
l = new.mergeTwoLists(key, key1)
l.printList(l)




