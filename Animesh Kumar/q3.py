import sys

class Node:                     #Node Class
    def __init__(self,val):
        self.value= val
        self.left=None
        self.right=None
def BSTchecker(node):#assuming left is always lesser
    if node is None:
        print("ERROR")
    if node.left is not None:
        if node.left.value <= node.value:
            BSTchecker(node.left)
        else:
            print("not a BST")
            sys.exit(0)
    if node.right is not None:
        if node.right.value> node.value:
            BSTchecker(node.right)
        else:
            print("not a BST")
            sys.exit(0)
root=Node(50)
root.left = Node(40)
root.right= Node(60)
root.left.left= Node(70)
BSTchecker(root)
print("Bst")
        
    

