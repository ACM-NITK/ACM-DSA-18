#Assignment 2
#Tejas C

class SNode:
 
    def __init__(self, data):
        self.data = data 
        self.next = None
 
class Stack:

    def __init__(self):
        self.top = None
 
    def isEmpty(self):
        return True if self.top is None else  False
 
    def push(self, data):
        temp = SNode(data)
        temp.next = self.top 
        self.top = temp
     
    def pop(self):
        temp = self.top 
        self.top = self.top.next
        popped = temp.data
        return popped
     
class Queue:
    
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()
    
    def enQueue(self,data):
        self.stack1.push(data)
    
    def deQueue(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            print("Q is empty")
            return
        if(self.stack2.isEmpty()):
            while (not self.stack1.isEmpty()):
                x=self.stack1.pop()
                self.stack2.push(x)
        x=self.stack2.pop()
        return x
    
    def front(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            print("Q is empty")
            return
        if(self.stack2.isEmpty()):
            while (not self.stack1.isEmpty()):
                x=self.stack1.pop()
                self.stack2.push(x)
        x=self.stack2.pop()
        self.stack2.push(x)
        return x  

#Driver Function

myQueue = Queue()
myQueue.enQueue(5)
myQueue.enQueue(10)
myQueue.enQueue(15)
print("Front element")
print(myQueue.front())
print("Dequeue")
print(myQueue.deQueue())
print(myQueue.deQueue())
print(myQueue.deQueue())

    