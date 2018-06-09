class Node:
    def __init__(self,prnt=None,val=None):
        self.parent=prnt
        self.value=val
        self.left=None
        self.right=None
    def inorder(self):
        if self==None:
            return
        if self.left!=None:
            self.left.inorder()
        print(self.value,end=' ')
        if self.right!=None:
            self.right.inorder()
    def preorder(self):
        if self==None:
            return
        print(self.value,end=' ')
        if self.left!=None:
            self.left.preorder()
        if self.right!=None:
            self.right.preorder()
class BST:
    def __init__(self):
        self.root=Node()

    def insert(self,x):
        if self.root.value==None:
            self.root.value=x
        else:
            p=self.root
            while True:
                if x<p.value:
                    if p.left==None:
                        p.left=Node(p,x)
                        break
                    else:
                        p=p.left
                elif x>p.value:
                    if p.right==None:
                        p.right=Node(p,x)
                        break
                    else:
                        p=p.right
                else:
                    print(x,"is already inserted.")
                    return
        print(x,"is Inserted.")

    def search(self,x,t):
        """search with t==1 prints the print statement where t!=1 doesn't...
        it is useful in second line of delete function."""
        p=self.root
        while True:
            if p.value==x:
                if t==1:
                    print(x,"is found!!!")
                return True
            else:
                if x<p.value:
                    if p.left!=None:
                        p=p.left
                    else:
                        if t==1:
                            print(x,"is not found!!!")
                        return False
                else:
                    if p.right!=None:
                        p=p.right
                    else:
                        if t==1:
                            print(x,"is not found!!!")
                        return False

    def delete(self,x):
        if not self.search(x,0):
            print(x,"is not exist in the tree.")
            return
        else:
            p=self.root
            t=0
            if self.root.value!=x:
                while True:
                    if p.value==x:
                        break
                    elif p.value<x:
                        p=p.right
                        t=0
                    elif p.value>x:
                        p=p.left
                        t=1
            if p.right==None:
                if p.left!=None:
                    p.left.parent=p.parent
                if t==1:
                    p.parent.left=p.left
                else:
                    p.parent.right=p.left
            else:
                k=p.right
                while k.left!=None:
                    k=k.left
                if k.right!=None:
                    k.right.parent=k.parent
                k.parent.left=k.right
                k.left=p.left
                k.right=p.right
                k.parent=p.parent
                p.left.parent=k
                p.right.parent=k
                if p==self.root:
                    self.root=k
                elif t==1:
                    p.parent.left=k
                else:
                    p.parent.right=k
            if __name__=="__main__":
                print(x,"is deleted.")
    def inorder(self):
        print("Inorder Traversal:",end=' ')
        self.root.inorder()
        print()
    def preorder(self):
        print("Preorder Traversal:",end=' ')
        self.root.preorder()
        print()
def main():
    T=BST()
    T.insert(50)
    T.insert(25)
    T.insert(100)
    T.insert(11)
    T.insert(35)
    T.insert(75)
    T.insert(150)
    T.insert(1)
    T.insert(13)
    T.insert(32)
    T.insert(45)
    T.insert(61)
    T.insert(80)
    T.insert(115)
    T.insert(200)
    print()
    print()
    T.inorder()
    T.preorder()
    T.search(32,1)
    T.search(70,1)

    T.delete(100)
    m=T.root.right
    print(m.value)
    print(m.left.value)
    print(m.right.value)
    """last four statements are added to check the delete operation and an image also added
    for reference.
    tree is drawn in the image."""

if __name__=='__main__':
    main()

                
