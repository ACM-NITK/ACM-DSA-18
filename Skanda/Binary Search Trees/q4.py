
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
            self.root=BSTnode(data)
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

    def range(self,a,b,node):
        ''' numbers between a and b. a,b included.  '''
        if node==None:
            return 0
        elif node.data<a:               # can be made <= if a has to be excluded
            return self.range(a,b,node.right)
        elif node.data>b:               # can be made >= if b has to be excluded
            return self.range(a,b,node.left)
        else:
            return 1+self.range(a,b,node.left)+self.range(a,b,node.right)


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


''' range test '''

print('Range test: ')
print('6 to 31: ',bst1.range(6,31,bst1.root))               # 13
print('-5 to 100: ',bst1.range(-5,100,bst1.root))               # 18
print('-10 to 29: ',bst1.range(-10,29,bst1.root))               # 13
print('12 to 40: ',bst1.range(12,40,bst1.root))               # 13
print('27 to 28: ',bst1.range(27,28,bst1.root))               # 0
print('11 to 35: ',bst1.range(11,35,bst1.root))               # 12
