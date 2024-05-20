#Leetcode 206. Reverse Linked List.
#https://leetcode.com/problems/reverse-linked-list/description/
#Given the head of a singly linked list, reverse the list, and return the reversed list.


class node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def printLinkedList(node):
    s = ''
    while node:
        s = s + str(node.val) + ' -> '
        node = node.next
    s = s + 'None'
    print(s)

#make a linked list of size n with random values
def initList(n):
    import numpy as np

    nodeList = []
    for i in range(0,n):
        v = np.random.random()
        nod = node(v)
        nodeList.append(nod)

    for i in range(0,len(nodeList)-1):
        nodeList[i].next = nodeList[i+1]

    return nodeList[0]


#This function reverses a linked list
def reverse(node):

    L, R = None, node

    while R:
        node = node.next
        R.next = L
        L = R
        R = node

    return L

v = initList(6)
print('Before reversing: ')
printLinkedList(v)
v = reverse(v)
print('After reversing: ')
printLinkedList(v)
