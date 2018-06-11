class Node:
 
    def __init__(self, data):
        self.data = data  
        self.next = None  
 
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next
 
    def append(self,data):
        temp = self.head
        if temp is not None:
            while temp.next != None:
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

    def InsertatIndex(self,i,data):
        new_node = Node(data)
        temp = self.head
        for x in range(1,i):
            temp = temp.next       
        new_node.next = temp.next
        temp.next = new_node

    def length(self):
        length = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            length += 1
        return length 

 
class Stack:

    def __init__(self):
        self.items = LinkedList()
        self.top = self.items.head

    def push(self,data):
        self.items.append(data)

    def pop(self):
         return self.items.deleteLast()

    def peek(self):
        temp = self.items.head
        while temp.next is not None:
            temp = temp.next
        print(temp.data)

    def size(self):
        return self.items.length() 

    def is_empty(self):
        if self.items.head is None:
            return True
        else:
            return False

    def print(self):
        self.items.printList()

class QueueUsingStack:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, data):
        self.stack_1.push(data)

    def dequeue(self):
        if not self.stack_1.is_empty():
            while self.stack_1.size() > 0:
                self.stack_2.push(self.stack_1.pop())
            res = self.stack_2.pop()
            while self.stack_2.size() > 0:
                self.stack_1.push(self.stack_2.pop())
            return res  


    def front(self):
        return self.stack1.items.head

    def printQueue(self):
        self.stack_1.print()
        # self.stack_2.print()
        # print(self.stack_1.size())

if __name__ == '__main__':
    
    q = QueueUsingStack()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    q.printQueue()



