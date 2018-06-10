
class BSTnode:
    def __init__(self,data=None,parent=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent

class BST:
    def __init__(self):
        self.root=None

    def insert (self,data,node):
        if node==None:
            self.root=BSTnode(data,self.root)
        elif data<=node.data:
            if node.left==None:
                node.left=BSTnode(data,node)
            else:
                self.insert(data,node.left)
        else:
            if node.right==None:
                node.right=BSTnode(data,node)
            else:
                self.insert(data,node.right)

    def search(self,data,node):
        if node==None:
            print('Not found.')
        elif data<node.data:
            self.search(data,node.left)
        elif data>node.data:
            self.search(data,node.right)
        else:
            print('Found')


    def delete(self,data,node):
        if node==None:
            print('Not found.')
        elif data<node.data:
            self.delete(data,node.left)
        elif data>node.data:
            self.delete(data,node.right)
        else:
            if node.left==node.right==None:
                if data<=node.parent.data:
                    node.parent.left=None
                else:
                    node.parent.right=None
            elif node.left==None:
                if data<node.parent.data:
                    node.right.parent=node.parent
                    node.parent.left=node.right
                else:
                    node.right.parent=node.parent
                    node.parent.right=node.right
            elif node.right==None:
                if data<=node.parent.data:
                    node.left.parent=node.parent
                    node.parent.left=node.left
                else:
                    node.left.parent=node.parent
                    node.parent.right=node.left
            else:
                node.data=self.max(node.left)
                self.delete(node.data,node.left)
                
    def preorder_traversal(self,node):
        print('-->',node.data,end=' ')

        if node.left!=None:
            self.preorder_traversal(node.left)
            
        if node.right!=None:
            self.preorder_traversal(node.right)

    def inorder_traversal(self,node):
        if node.left!=None:
            self.inorder_traversal(node.left)

        print('-->',node.data,end=' ')

        if node.right!=None:
            self.inorder_traversal(node.right)

    def max(self,node):
        if node==None:
            return None
        elif node.right==None:
            return node.data
        else:
            return self.max(node.right)

    def min(self,node):
        if node==None:
            return None
        elif node.left==None:
            return node.data
        else:
            return self.min(node.left)



''' test code '''

'''   The tree looks like this:
                                                                      25
                                                               /               \
                                                        10                        30
                                                    /        \                  /        \
                                                5           15            29           45
                                            /            /       \       /      \         /
                                        1             11        16  26     30     36
                                                          \           \                       \
                                                           12         20                     40
                                                        /      \
                                                      12      13
      
'''

bst1=BST()
bst1.insert(25,bst1.root)
bst1.insert(10,bst1.root)
bst1.insert(30,bst1.root)
bst1.insert(5,bst1.root)
bst1.insert(15,bst1.root)
bst1.insert(11,bst1.root)
bst1.insert(16,bst1.root)
bst1.insert(29,bst1.root)
bst1.insert(45,bst1.root)
bst1.insert(36,bst1.root)
bst1.insert(40,bst1.root)
bst1.insert(12,bst1.root)
bst1.insert(13,bst1.root)
bst1.insert(1,bst1.root)
bst1.insert(12,bst1.root)
bst1.insert(20,bst1.root)
bst1.insert(30,bst1.root)
bst1.insert(26,bst1.root)

''' insert test'''

print('Insert test: ')
print(bst1.root.data)
print(bst1.root.left.data)
print(bst1.root.right.data)
print(bst1.root.left.left.data)
print(bst1.root.left.right.data)
print(bst1.root.right.left.data)
print(bst1.root.right.right.data)
print(bst1.root.left.right.left.data)
print(bst1.root.left.right.right.data)
print()

''' search test '''

print('Search for: ')
print('25: ',end='')
bst1.search(25,bst1.root)
print('30: ',end='')
bst1.search(30,bst1.root)
print('26: ',end='')
bst1.search(26,bst1.root)
print('19: ',end='')
bst1.search(19,bst1.root)
print('11: ',end='')
bst1.search(11,bst1.root)
print('45: ',end='')
bst1.search(45,bst1.root)
print('0: ',end='')
bst1.search(0,bst1.root)
print('31: ',end='')
bst1.search(31,bst1.root)
print('16: ',end='')
bst1.search(16,bst1.root)
print()


''' preorder traversal '''
print('Preorder Traversal: ')           #  25,10,5,1,15,11,12,12,13,16,20,30,29,26,30,45,36,40 
bst1.preorder_traversal(bst1.root)
print()



''' inorder traversal '''
print('Inorder Traversal:')
bst1.inorder_traversal(bst1.root)               # numbers in increasing order
print()             #  1,5,10,11,12,12,13,15,16,20,25,26,29,30,30,36,40,45  




''' delete test '''

print()
print('Delete test:')

print('Deleted 10:')
bst1.delete(10,bst1.root)
print(bst1.root.left.data)           # 5

print('Deleted 45:')
bst1.delete(45,bst1.root)
print(bst1.root.right.right.data)           #  36
print(bst1.root.right.right.right.data)            # 40
print(bst1.root.right.data)            #30

print('Deleted 16:')
bst1.delete(16,bst1.root)
print(bst1.root.left.right.right.data)      #20
print(bst1.root.left.right.data)           # 15
print(bst1.root.left.right.left.data)           # 11

print('Deleted 25:')
bst1.delete(25,bst1.root)
print(bst1.root.data)               # 20






    
    
    


