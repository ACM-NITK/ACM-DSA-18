from Binary_Search_Tree import *
def checkNode(p,l,u):
    if p.left==None and p.right==None:
        return True
    if p.left!=None:
        if p.left.value<p.value and p.left.value>l:
            lc=checkNode(p.left,l,p.value)
        else:
            return False
    if p.right!=None:
        if p.right.value>p.value and p.right.value<u:
            rc=checkNode(p.right,p.value,u)
        else:
            return False
    if lc==True and rc==True:
        return True
    else:
        return False
        
def isBST(T):
    p=T.root
    return checkNode(p,float('-inf'),float('inf'))

def main():
    T=BST()
    T.insert(50)
    T.insert(25)
    T.insert(75)
    T.insert(10)
    T.insert(30)
    T.insert(60)
    T.insert(90)
    print("is this Tree BST?")
    print(isBST(T))

if __name__=='__main__':
    main()
