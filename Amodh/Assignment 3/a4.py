import a1

def countInRange(s,e,node): #here we take True to mean 1 and false to mean 0
    l = countInRange(s,e,node.left) if node.left is not None else 0     #get count on left part of tree by recursing
    r = countInRange(s,e,node.right) if node.right is not None else 0   #get count on right part of tree by recursing
    return (node.val>=s and node.val<=e)+l+r        #return sum of counts
    
def main():
    b = a1.Node(8)
    for i in [6,10,1,7,13]:
        b.insert(i)
    print(countInRange(1,11,b))
    
if __name__=='__main__':
    main()
