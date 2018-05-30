class Stack:
	"""various operations in stack implimented using linked list"""
	def __init__(self):
		self.top = Node()

	def push(self, x):
		temp = Node(x,self.top.next)
		self.top.next = temp

	def pop(self):
		self.top.next = self.top.next.next

	def peek(self):
		return self.top.next.value

	def isempty(self):
		if self.top.next == None:
			return True
		else:
			return False

class Queue:
	def __init__(self):
		self.front = Node()
		self.rear = Node()

	def enqueue(self, x):

		if self.front.next == None:
		    temp = Node(x, self.front.next)
		    self.front.next = temp
		    self.rear = temp
		else:
			temp = Node(x, self.rear.next)
			self.rear.next = temp

	def dequeue(self):
		self.front.next = self.front.next.next

	def Front(self):
		return self.rear.value

class Q_wid_Stacks:

	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()


	def enque(self, x):
		self.s1.push( x)

	def deque(self):
		if not self.s2.isempty():
			self.s2.pop()
		else:
			while not self.s1.isempty():
				self.s2.push( self.s1.peek())
				self.s1.pop()
			self.s2.pop()

	def frnt(self):
		if not self.s2.isempty():
			return self.s2.peek()
		else:
			while not self.s1.isempty():
				self.s2.push( self.s1.peek() )
				self.s1.pop()
			return self.s2.peek()




class Node:
	def __init__(self, val = None, nxt = None):
		self.value = val
		self.next = nxt

def main():

	s = Stack()

	print("checking stack using linked list")
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.pop()
	print(s.peek())

	print("checking queue using linked list")
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print ( q.Front())
	q.dequeue()
	print ( q.Front())
	q.dequeue()
	print ( q.Front())

	print("checking queue implemented using stack")
	new = Q_wid_Stacks()
	new.enque(11)
	new.enque(22)
	new.enque(33)
	new.enque(44)
	new.deque()
	print (new.frnt())
	new.deque()
	print (new.frnt())




if __name__ == '__main__':
	main()