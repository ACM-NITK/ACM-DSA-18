class LinkedList:
    """Defines a Singly Linked List.
    attributes: head - a pointer to the first node object
    """

    def __init__(self):
        self.head = ListNode()
        """ This is the constructor. It tells you what are the attributes of all objects belonging to this class. You do not need to call the constructor. """
        """Creates a new list as soon as an object is created with a Sentinel( head with no value ) Node"""

    def insert(self, x, p):
        temp = ListNode(x, p.next)
        p.next = temp
        """This insert function creates and inserts a new node at a position after a node "p" that exists in the code already"""

    def delete(self, p):
        p.next = p.next.next
        """Delete the node following node p in the linked list, by removing any reference to that node itself. """

    def printlst(self):
        it = self.head.next
        while it is not None:
            print(it.value, end=' ')
            it = it.next
        print("")
        """ Print all the elements of a list in a row."""

    def insertAtIndex(self, x, i):
        it = self.head
        for m in range(0, i):
            it = it.next
        temp = ListNode(x, it.next)
        it.next = temp
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""

    def search(self, x):
        it = self.head.next
        ret = None
        while ret is None:
            if it.data == x:
                ret = it
            else:
                it = it.next
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        return (ret)


    def len(self):
        it = self.head
        ans = 0
        while it.next is not None:
            ans += 1
            it = it.next
        """Return the length (the number of elements) in the Linked List."""
        return ans


    def isEmpty(self):
        if self.head.next is None:
            return True
        else:
            return False
        """Return True if the Linked List has no elements, False otherwise."""



class ListNode:
    """Represents a node of a Singly Linked List.
    attributes: value, next - reference that points to the next node in the list.
    """

    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt


def main():
    L = LinkedList()
    L.insert(10, L.head)
    print('List is: ', end='')
    L.printlst()
    L.insert(12, L.head.next)
    print('List is: ', end='')
    L.printlst()
    L.insert(2, L.head)
    print('List is: ', end='')
    L.printlst()
    print('Size of L is ', L.len())
    L.delete(L.head)
    print('List is: ', end='')
    L.printlst()
    L.delete(L.head.next)
    print('List is: ', end='')
    L.printlst()
    print('List is empty?', L.isEmpty())
    print('Size of L is ', L.len())
    L.delete(L.head)
    print('List is empty?', L.isEmpty())
    print('Size of L is ', L.len())
    L.insertAtIndex(2, 0)
    L.insertAtIndex(1, 0)
    L.insertAtIndex(4, 2)
    L.insertAtIndex(3, 2)
    print('List is: ', end='')
    L.printlst()

if __name__ == '__main__':
main()
