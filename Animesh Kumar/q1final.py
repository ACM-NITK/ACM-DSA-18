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
    def search(self,value,node):        #binary search
        if self.root is None:
            print("Binary tree error")
        elif value<node.value:
            if node.left is not None:
                self.search(value,node.left)
            else:
                print("Unsuccessful")
        elif value> node.value:
            if node.right is not None:
                self.search(value,node.right)
            else:
                print("Unsuccessful")
        else:
            print("Successful")
            
    def preOrder_transversal(self,node):
        if node is None:
            return
        print("-->",node.value,end='')
        self.preOrder_transversal(node.left)
        self.preOrder_transversal(node.right)
    def inOrder_tranversal(self,node):
        if node is None:
            return
        self.inOrder_tranversal(node.left)
        print("-->",node.value,end='')
        self.inOrder_tranversal(node.right)
        
    def minNode(self,node):             #to find minimum node in the right subtree
        current = node.right
        while (current.left is not None):
            current = current.left
        return current
        
    def delete(self,value,node,parent=None):        #deletion 
        if node is None:
            print("Deletion Error")
            return 
        if node.value> value:
            self.delete(value,node.left,node)
        elif node.value< value:
            self.delete(value,node.right,node)
        else:
            if node.left is None:               #one child and no child case
                if parent.value>node.value:
                    parent.left= node.right
                else:
                    parent.right=node.right
            elif node.right is None:
                if parent.value>node.value:
                    parent.left= node.left
                else:
                    parent.left=node.left
            else:                           #two child case
                temp=self.minNode(node)
                node.value=temp.value
                self.delete(temp.value,node.right,node)
                
def main():
    """populating the tree"""
    b1=BST()
    k=[50,40,21,22,8,45,61,43,25,48,63,74,55,68]
    for i in k:
        b1.insert(i,b1.root)
        
        """tree should look like this
                            50
                        /       \
                      40          61
                   /       \       /   \
                21        45        55  63
                / \       / \               \
                8   22    43 48               74
                     \                    /
                      25              68
        
        
        
        
        
        
    """preorder transversal"""
    
    print("Preorder Transversal:")
    b1.preOrder_transversal(b1.root)
    
    """Inorder Transversal"""
    print("\nInorder Transversal:")
    b1.inOrder_tranversal(b1.root)
    print()
    
    """Unsuccessful Deletion"""
    b1.delete(10,b1.root)
    
    """Successful Deletion"""
    b1.delete(21,b1.root)
    b1.preOrder_transversal(b1.root)
    print()
   
    "Unsuccessful search"""
    b1.search(24,b1.root)
    
    """Successful Search"""
    b1.search(45,b1.root)
    
    
    
if __name__=='__main__':
    main()

        