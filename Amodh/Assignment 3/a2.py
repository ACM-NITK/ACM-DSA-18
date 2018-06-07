import a1
def makeBST(a):
    if len(a)==1:
        return a1.Node(a[0])
    t = a1.Node(a[len(a)//2])   #inserting middle element into tree
    t.left = makeBST(a[:len(a)//2])     #recursing function with first half of list 
    t.right = makeBST(a[(len(a)//2)+1:]) if (len(a)//2)+1<len(a) else None          #recursing function with second half of list
    return t
    
def main():
    l = [1,6,7,8,10,13]
    root = makeBST(l)
    root.inOrder()
    
if __name__=='__main__':
    main()
