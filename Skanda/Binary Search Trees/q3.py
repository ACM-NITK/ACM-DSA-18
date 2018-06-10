
class BSTnode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

''' Makes use of inorder traversal and checks if the elements are in increasing order '''
previous=None

def is_not_bst(node):
    if node==None:
        return
    if is_not_bst(node.left):
        return True
    global previous
    try:
        if previous>node.data:
            return True
        previous=node.data
    except:
        previous=node.data
    if is_not_bst(node.right):
        return True


''' Sample binary tree ---NOT a bst '''

bst=BSTnode(25)
bst.left=BSTnode(11)
bst.right=BSTnode(39)
bst.left.left=BSTnode(5)
bst.left.right=BSTnode(15)
bst.left.right.left=BSTnode(12)
bst.left.right.right=BSTnode(20)
bst.right.left=BSTnode(36)
bst.right.right=BSTnode(40)
bst.right.right.left=BSTnode(10)



if is_not_bst(bst):
    print('Not a bst.')
else:
    print('It is a bst.')







