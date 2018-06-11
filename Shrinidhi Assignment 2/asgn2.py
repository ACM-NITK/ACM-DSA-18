class Node:
    '''Linked List program which has been added from the first week assignment '''
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printlst(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next
            
    def append(self,data):
        temp = self.head
        if temp is not None:
            while temp.next!=None:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.head = Node(data)
            
    def insert(self,data,node):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        
    def delete(self,prev_node):
        prev_node.next = prev_node.next.next
        
    def deleteLast(self):
        temp = self.head
        if temp.next is not None:
            while temp.next.next is not None:
                temp = temp.next
            val = temp.next.data
            temp.next = None
            return val
        elif self.head is None:
            return None
        elif self.head.next is None:
            value = self.head.data
            self.head = None
            return value
        
    def InsertatIndex(self,it,data):
        new_node = Node(data)
        temp = self.head
        for x in range(1,it):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def length(self):
        length = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            length = length + 1
        return length
        

class Stack:
    '''This class will be used in future for pushing and popping elements from a stack of items'''
    def __init__(self):
        self.item = LinkedList()
        self.top = self.item.head
        
    def push(self,data):
        self.item.append(data)
        
    def pop(self):
        return self.item.deleteLast()
        
    def peek(self):
        temp = self.item.head
        while temp.next is not None:
            temp = temp.next
        print(temp.data)
    
    def size(self):
        return self.item.length()
        
    def is_empty(self):
        if self.item.head is None:
            return True
        else:
            return False
            
    def print(self):
        self.item.printlst()
        
class QueueStack:
    ''' here the logic which is used is to perform queue operation using two stacks .
    this can be done by pushing an element x in stack 1. after pushing N elements in 
    stack 1 (equivalent to enqueue operation performed in case of a queue ), we need 
    to pop out each element from stack 1 and push it in stack 2 .
    Now the elements present in stack 1 are arranged in exact reverse order.
    Now if we pop out each element from stack 2 , its performing an operation which is 
    equivalent to dequeue operation in a queue data structure. Hence a queue
    data structure can be implemented using two stacks in least possibe time. '''
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self,data):
        self.stack1.push(data)
    
    def dequeue(self):
        if not self.stack1.is_empty():
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            res = self.stack2.pop()
            
            ''' here we are performing the operation of pop an element x from
               stack 1 and pushing the same element in stack 2. this is performed for all 
               the stack 1 elements. Now the top element of stack 2 is the first
               element which was pushed in stack 1.'''
               
            
            ''' here we are popping out the topmost element of stack 2. this is like removing
            the first element to be entered in stack 1. hence dequeue operaton is performed'''
            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())
            return res
        if self.stack2.size() <= 0:
                print("Underflow!")
            
    def front(self):
        return self.stack1.item.head
        
    def printQueue(self):
        self.stack1.print()
        
if __name__=='__main__':
    q = QueueStack()
    q.enqueue(100)
    q.enqueue(1999)
    q.enqueue(4)
    q.enqueue(11)
    print("\nNow let us print the queue after performing enqueue operation on the above elements.\n")
    q.printQueue()
    print("\nNow we are performing dequeue operation on the queue and printing the same queue. Just observe the change.\n")
    q.dequeue()
    print("\nList is: ")
    q.printQueue()
    q.dequeue()
    print("\nList is: ")
    q.printQueue()
    q.dequeue()
    print("\nList is: ")
    q.printQueue()
    q.dequeue()
    print("\nList is: ")
    q.printQueue()
    q.dequeue()
    