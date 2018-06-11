class Stack:
    """attributes are top to represent the first node, while enqueue in list it will be done
    similar to push in stack but when dequeue , the stack will be reversed and saved in another
    stack and then pop will be used"""

    def __init__(self):
        self.top=Node()


    def push(self,d):
        f=Node(d,self.top)
        self.top=f


    def pop(self):
        if(self.top.nxt is None ):
            return False
        else:
            x=self.top.data
            self.top=self.top.nxt
            return x
            

    def peek(self):
        if(self.top.nxt is not None ):
            return self.top.data
        else:
            return False




class q:
    """this is the class whose instance will serve as a queue"""


    def __init__(self):
        """initialize the 2 stacks"""
        self.s1=Stack()
        self.s2=Stack() 


    def enq(self,d):
        """this method enqueues data in the rear of the queue"""
        if(self.s2.top.nxt is not None):
            self.trans(self.s2,self.s1)

        self.s1.push(d)

        
    def trans(self,a,b):
        """this method transfers the content of one stack to another i.e. reverses one stack and save it in another stack"""
        while a.top.nxt is not None:
            b.push(a.pop())

                    
    def deq(self):
        """this method removes data from the front of the list and returns it"""
        if(self.s2.top.nxt is None):
            """transfer from s1 to s2, then s1 empty and s1 reversed stored in s2"""
            self.trans(self.s1,self.s2)
            
        """now pop from s2 to get the front of queue"""
        return (self.s2.pop())



    def front_(self):
        """this method returns the data from the front of the queue but does not removes it"""
        if(self.s2.top.nxt is None):
            """transfer from s1 to s2, then s1 empty and s1 reversed stored in s2"""
            self.trans(self.s1,self.s2)
            
        """now pop from s2 to get the front of queue"""
        return (self.s2.peek())



class Node:
    """this class creates instances for node"""

    def __init__(self,data=None,nxt=None):
        self.data=data
        self.nxt=nxt




def main():
    """q1 denotes the queue"""
    q1=q()
    
    """menu driven -> ask user whether to enqueue , dequeue or just see the front element"""
    while True:
        print("\n1 enqueue\n2 dequeue\n3 front\n anything else exit: ")
        x=int(input())
        if(x==1):
            y=input("\nenter data : ")
            q1.enq(y)
            
        elif x==2:
            r=q1.deq()
            if(r is False):
                print("\nqueue empty")
            else:
                print(f"\ndequeued data : {r}")
    
            
        elif x==3 :
            r=q1.front_()
            if(r is False):
                print("\nqueue empty")
            else:
                print(f"\nfront data : {r}")
    
        else:
            break



if __name__ == '__main__':
    main()
