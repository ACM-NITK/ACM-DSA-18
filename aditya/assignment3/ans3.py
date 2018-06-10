import ans1
        
def getList(node,l):#returns the tree in-order
    if node.left:#first the left node
        l = getList(node.left,l)
    l.append(node.val)#then the middle node
    if node.right:#then finally the last node
        l = getList(node.right,l)
    return l    
    
def isBST(node):
    l = getList(node,[]) #stores the tree in-order
    if sorted(l)==l: # an in-ordered BST is always sorted
        return True
    else:
        return False

def main():
    t1 = ans1.Node(8) 
    l = [6,10,1,7,13]
    for i in l:
        t1.insert(i)
    print(isBST(t1))
    t2 = ans1.Node(8)
    t2.left = ans1.Node(10)
    t2.right = ans1.Node(5)
    t2.left.left = ans1.Node(1)
    t2.left.right = ans1.Node(12)
    t2.right.left = ans1.Node(4)
    t2.right.right = ans1.Node(8)
    print(isBST(t2))
    
if __name__=='__main__':
    main()

