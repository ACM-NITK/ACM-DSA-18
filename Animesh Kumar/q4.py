
class Node:                     #Node Class
    def __init__(self,val):
        self.value= val
        self.left=None
        self.right=None
        
class BST:                      #treeClass
    def __init__(self):
        self.root=None
        
    def insert(self,value,node):
        if self.root is None:       #inserting the root
            self.root=Node(value)
        elif value<=node.value:         #recursing for value less than node
            if node.left is not None:
                self.insert(value,node.left)
            else:
                node.left=Node(value)   #recursing for values greater than node
        elif value>node.value:
            if node.right is not None:
                self.insert(value,node.right)
            else:
                node.right=Node(value)
    def searchrange(self,node,a,b):  #including end values
        if node==None:
            return 0
        elif node.value<a:
            return self.searchrange(node.right,a,b)
        elif node.value>b:
            return self.searchrange(node.left,a,b)
        else:
            return 1+self.searchrange(node.left,a,b)+ self.searchrange(node.right,a,b)
            
            
def main():
    """populating the tree"""
    b1=BST()
    k=[50,40,21,22,8,45,61,43,25,48,63,74,55,68]
    for i in k:
        b1.insert(i,b1.root)   
    """search range between 20 to 40"""
    print(b1.searchrange(b1.root,20,40))
if __name__=='__main__':
    main()


