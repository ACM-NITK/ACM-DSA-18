
class BSTnode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


sorted_array=[]
n=int(input('Enter number of elements: '))
for i in range(n):
    sorted_array.append(int(input('Enter element %d' %(i+1)+': ')))

root=BSTnode(sorted_array[0])
node=root

# assuming increasing array
for x in sorted_array[1:]:
    node.right=BSTnode(x)
    node=node.right

print('Following is the tree (consecutive right nodes): ')
''' Printing all the consecutive right nodes '''
node=root
while node:
    print('-->',node.data,end='')
    node=node.right
    
    
