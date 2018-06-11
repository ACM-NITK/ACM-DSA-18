import LL # this is the linked list script provided in the beginning, renamed as LL

class Stack:
    def __init__(self):
        self.l = LL.LinkedList()
    
    def push(self,x):
        temp = self.l.head
        while temp.next!=None:
            temp = temp.next
        self.l.insert(x,temp) #inserting in the end
    
    def pop(self):
        temp = self.l.head
        if temp.next==None: #checking if stack is empty
            return None
        while temp.next.next!=None:
            temp = temp.next
        x = temp.next.value
        self.l.delete(temp) #deleting the last node
        return x
    
    def peek(self):
        temp = self.l.head
        if temp.next==None:#checking if stack is empty
            return None
        while temp.next!=None:
            temp = temp.next
        return temp.value#returning the value of the last node

class Queue:
    def __init__(self):
        self.inStack = Stack() #all input goes to this stack
        self.outStack = Stack() #all output comes from this stack
       
    def enqueue(self,x):
        self.inStack.push(x)#pushing into inStack
        
    def dequeue(self):
        if self.outStack.l.head.next==None:#checking if outStack is empty
            while self.inStack.l.head.next!=None: #if yes, then popping all members from inStack
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()#popping from outStack
            
    def front(self):
        if self.outStack.l.head.next==None:#checking if outStack is empty
            while self.inStack.l.head.next!=None:#if yes, then popping all members from inStack
                self.outStack.push(self.inStack.pop())
        return self.outStack.peek()#peeking from outStack
        
def main():
    Q = Queue()
    for i in range(1,6):
        Q.enqueue(i)#Queue now has [1<-2<-3<-4<-5]
    print(Q.front()) #prints 1
    Q.dequeue()#removes 1. Queue is now [2<-3<-4<-5]
    print(Q.front())#prints 2
    Q.dequeue()#removes 2. Queue is now [3<-4<-5]
    print(Q.front())#prints 3
         
         
if __name__=='__main__':
main()
