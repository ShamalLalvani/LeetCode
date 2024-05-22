#Leetcode 701. Insert into a binary search tree.
#https://leetcode.com/problems/insert-into-a-binary-search-tree/
#You are given the root node of a binary search tree (BST) and a value to insert into the tree.
#Return the root node of the BST after the insertion.
#It is guaranteed that the new value does not exist in the original BST.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def insert(root,val):

    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def initializeTree():
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    b.right = e
    b.left = d
    a.right = c
    a.left = b
    return a

def printTree(node,i):
    if node == None:
        #print('END Node')
        return
    else:
        s = ''
        for j in range(0,i):
            s+= ' '
        print(s,"Row ", str(i),': ',node.val)
        printTree(node.left,i+1)
        printTree(node.right,i+1)


a = initializeTree()
print("Before Inserting: ")
printTree(a,0)
b = insert(a,8)
print("After Inserting: ")
printTree(b,0)
