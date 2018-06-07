class Node:
    def __init__(self,val = 0):
        self.val = val
        self.right = None
        self.left = None
        
    def insert(self,val):                #inserting into the BST
        if self.val<val:                    #moving right along the tree
            if self.right is not None: #if right node exists
                self.right.insert(val)
            else:
                self.right = Node(val)
        elif self.val>val:                  #moving left along the tree
            if self.left is not None:   #if left node exists
                self.left.insert(val)
            else:                                   
                self.left = Node(val)
        else:                                   #if node value is same as new node value
            temp = Node(val)
            temp.left = self.left
            self.left = temp
            
    def delete(self,val):
        if self.val == val:             #if the node is found
            if self.left and self.right: #if node has both children
                p ,s = self.right.minandparent(self)#successor and parent of successor
                if p.left == s:         #if successor is not immediately to right of node to be deleted
                    p.left = s.right
                else:                       #if successor is immediately to right of node to be deleted
                    p.right = s.right
                s.right = self.right            #replacing node with successor node
                s.left = self.left
                return s
            elif self.left:                 #if only left child exists
                self = self.left
            else:                              #if only right child exists
                self = self.right      
        elif self.val>val:              #if node not found and current node value is more than value to be deleted
            if self.left:
                self.left = self.left.delete(val)
            else:
                print("Node not found")
        else:                                  #if node not found and current node value is less than value to be deleted
            if self.right:
                self.right = self.right.delete(val)
            else:
                print("Node not found")
        return self
                    
    def minandparent(self,p):#returns smallest node in the given tree along with its parent
        if self.left:                   #if smaller node exists, move left
            return self.left.minandparent(self)
        else:                               #else return current node and its parent
            return p,self
            
    def preOrder(self):                 #pre order traversal
        print(self.val, end = " ")
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()
            
        
    def inOrder(self):                  #in order traversal
        if self.left is not None:
            self.left.inOrder()
        print(self.val,end = " ")
        if self.right is not None:
            self.right.inOrder()
            
    def Search(self,val):
        if self.val == val:             #if found, return that node
           return self
        elif self.val<val:              #if node val less than search element, move right
            if self.right is not None:
                return self.right.Search(val)
            else:
                return None
        else:                                   #if node val more than search element, move left
            if self.left is not None:
                return self.left.Search(val)
            else:
                return None
                
def main():
    b = Node(8)
    a = [6,10,1,7,13]
    for i in a:
        b.insert(i)
    b.inOrder()
    print("")
    b.preOrder()
    print("")
    b = b.delete(100)
    b.inOrder()
    print("")
    
    
if __name__=='__main__':
    main()
