from Binary_Search_Tree import *
def itr(l,u,inList,tree):
    if u-l==0:
        tree.insert(inList[l])
    elif u-l==1:
        tree.insert(inList[l])
        tree.insert(inList[u])
    else:
        m=l+int((u-l)/2)
        tree.insert(inList[m])
        itr(l,m-1,inList,tree)
        itr(m+1,u,inList,tree)
    """This Function iterates through all elements
    of the list in the manner that binary tree can be formed"""
def listToTree(inList):
    inList.sort()
    tree=BST()
    l=0
    u=len(inList)-1
    itr(l,u,inList,tree)
    return tree
def main():
    L=[100,50,150,25,75,125,175,10,40,60,90,110,140,160,190]
    T=listToTree(L)

if __name__=='__main__':
    main()

