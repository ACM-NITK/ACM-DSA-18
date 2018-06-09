from Binary_Search_Tree import *
from BST_from_sorted_List import *

def itrn(p,l,u):
    if p.value<l:
        if p.right!=None:
            return itrn(p.right,l,u)
        else:
            return 0
    elif p.value>u:
        if p.left!=None:
            return itrn(p.left,l,u)
        else:
            return 0
    else:
        if p.right!=None:
            if p.left!=None:
                return 1+itrn(p.left,l,u)+itrn(p.right,l,u)
            else:
                return 1+itrn(p.right,l,u)
        else:
            if p.left!=None:
                return 1+itrn(p.left,l,u)
            else:
                return 1

def NoOfNodes(tree,l,u):
    p=tree.root
    return itrn(p,l,u)
    """var l is lower limit and var u is upper limit"""
    
def main():
    T=BST()
    T=listToTree([5,10,15,25,27,30,35,50,55,60,65,75,80,90,95])
    print("No of Nodes Which have value between 11 and 65 are...",NoOfNodes(T,11,65),sep='\n')
if __name__=='__main__':
    main()
    
