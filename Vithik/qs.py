class Stack:
    """Defines a Stack linked list
    attributes: top - a pointer to the first node object
    """

    def __init__(self):
        
        self.top=None
       
    def push(self,x):#push inside stack
        
        if self.top==None:
            self.top=ListNode(x)
        else:
            temp=ListNode(x,self.top)
            self.top=temp


    def pop(self):#pop from stack
        if self.top==None:
            return 0
        else:
            x=self.top.value
            self.top=self.top.next
            return x


    def peek(self):#peek the element from stack
        if self.top==None:
            print(' empty')
        else:
            return self.top.value


    

    def len(self):#length of stack
        it = self.top
        ans = 0
        while it is not None:
            ans =ans + 1
            it = it.next
        """Return the length (the number of elements) in the Linked List."""
        return ans

     
            
        
        
            
        
class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next - reference that points to the next node in the list.
    """

    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt


class Queue:

    def __init__(self):
        self.qu=Stack()

    def enqueue(self,x):
        self.qu.push(x)


    def dequeue(self):#popping the first come element
        

        if(self.qu.len()==0):
            print("Queue empty")


        elif(self.qu.len()==1):
            y=self.qu.pop()
            print(y,"is dequeued")

        else:
            x=self.qu.pop()
            self.dequeue()
            self.qu.push(x)



    def fron(self):#same as popping method but just peeking it
        

        if(self.qu.len()==0):
            print("Queue empty")


        elif(self.qu.len()==1):
            y=self.qu.peek()
            print(y,"is the front element")

        else:
            x=self.qu.pop()
            self.fron()
            self.qu.push(x)

        

def main():
    L=Queue()
    L.enqueue(10)
    L.enqueue(20)
    L.enqueue(30)
    L.fron()
    L.dequeue()
    
    L.fron()
    L.dequeue()
    L.fron()
    L.dequeue()
    L.fron()
    
    
    



if __name__ == '__main__':
    main()





            
        
    

    
                        

        


  



    
            
            
            
        


        

    
        


   

    
    




