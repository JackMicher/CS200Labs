# Jack Micher
# 9/30/2020
# CS/IT 200-03

class LeakyArrayStack:
    """Stack implementation taken from array_stack.py modified to leak"""
    
    def __init__(self, maxsize):
        """
        Stack Constructor
        maxsize: inputs max size of the leaky stack (amount that the stack can hold before ejecting elements)
        """
        if isinstance(maxsize, int) == False: # Check to see if input of stack size is valid
            raise TypeError('Invalid input, input size must be an integer')
        if maxsize <= 0: # Check to see if input of stack size is above 0
            raise ValueError('Invalid size, must be above 0')
        self._size = 0              # Current Size value for stack
        self._maxsize = maxsize     # Maximum capcity of stack
        self._data = [None]*maxsize # Underlying array set to size of maximum capacity
        self._top = 0               # Index pointer to the element at the top of the stack

    def push(self, e):
        """
        Push element on top of the stack
        e: Add element e to the top of the stack
        Remove element at the bottom of the stack when reaching max capacity
        """
        if self._size == 0: # Special case if list is empty to keep top pointer in place
            self._data[self._top] = e
            self._size += 1
            return
        self._top = (self._top + 1) % self._maxsize
        self._data[self._top] = e
        if self._size < self._maxsize:
            self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack."""
        if self.is_empty(): # Check if empty, return error if true
            raise IndexError('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element at the top of the stack."""
        if self.is_empty(): # Check if empty, return error if true
            raise IndexError('Stack is empty')
        temp = self._data[self._top]
        self._data[self._top] = None
        self._top = self._top - 1 # A quirk of this is the pointer will go back one regardless if size is 0, but it overall doesn't matter
        if self._top < 0:
            self._top = self._maxsize - 1
        self._size -= 1
        return temp
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    
    def __len__(self):
        """Return total size of the stack"""
        return self._size
    
    def __str__(self):
        """Return string of stack w/ elements"""
        return str(self._data)



class LeakyLinkedStack:
    
    class _Node:
        """Doubly linked node class"""

        def __init__(self, e, n, p):
            """
            Node Constructor
            e: Assign element item of node
            n: Next node of this node is n
            p: Previous node of this node is p
            """
            self._element = e   # Element item of node
            self._next = n      # Reference to next node
            self._prev = p      # Reference to previous node

    def __init__(self, maxsize):
        self._head = None       # Reference to head node
        self._size = 0          # Number of stack elements
        self._tail = None       # Reference to tail node
        self._maxsize = maxsize # Maximum capacity of stack

    def push(self, e): # FIXME: Modify to remove from beginning based on delcared size and also use tail
        """
        e: Add element e to the top of the stack
        """
        if self._size == 0:
            self._head = self._Node(e, None, None)
            self._tail = self._head
        else:
            current = self._Node(e, None, self._tail)
            self._tail._next = current
            self._tail = current
            
        if self._size == self._maxsize:
            current = self._head._next
            current._prev = None
            self._head._next = None
            self._head = current
        else:
            self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise IndexError if the stack is empty.
        """
        if self.is_empty(): # Check if empty, return error if true
            raise IndexError('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element at the top of the stack"""
        if self.is_empty(): # Check if empty, return error if true
            raise IndexError('Stack is empty')
        temp = self._tail._element
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            current = self._tail._prev
            current._next = None
            self._tail._prev = None
            self._tail = current
        self._size -= 1
        return temp
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    
    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size
    
    def __str__(self):
        """Return string of stack w/ elements"""
        if self.is_empty():
            return '[]'
        string = '['
        current = self._head
        while current is not None:
            string += str(current._element)
            current = current._next
            if current is not None:
                string += ', '
        string += ']'
        return string

def main():
    print("========== Testing Leaky Array Stack ==========")
    jah = LeakyArrayStack(4) # Create Leaky Array Stack with a maximum size of 4
    print("------------- Pushing...") # Push in 5 elements
    print(jah)
    jah.push('1st')
    print(jah)
    jah.push('2nd')
    print(jah)
    jah.push('3rd')
    print(jah)
    jah.push('4th')
    print(jah)
    jah.push('5th')
    print(jah)
    print("Size: {}".format(str(len(jah))))
    print("------------- Popping...") # Pop 3 elements
    jah.pop()
    print(jah)
    print("Size: {}".format(str(len(jah))))
    jah.pop()
    print(jah)
    print("Size: {}".format(str(len(jah))))
    jah.pop()
    print(jah)
    print("Size: {}".format(str(len(jah))))
    print("------------- Pushing...") # Push in 4 elements
    jah.push('6th')
    print(jah)
    jah.push('7th')
    print(jah)
    jah.push('8th')
    print(jah)
    jah.push('9th')
    print(jah)
    print("------------- Popping...") # Pop 4 elements, causing list to be empty
    jah.pop()
    print(jah)
    jah.pop()
    print(jah)
    jah.pop()
    print(jah)
    jah.pop()
    print(jah)
    #jah.pop() the empty stack here to test for the IndexError
    print("Size: {}".format(str(len(jah))))
    print("------------- Pushing...") # Push in 1 element
    jah.push('10th')
    print(jah) # Front index will be moved forward
    
    print()
    
    print("========== Testing Leaky Linked Stack ==========")
    seh = LeakyLinkedStack(4)
    print("------------- Pushing...") # Push in 5 elements
    seh.push('1st')
    print(seh)
    seh.push('2nd')
    print(seh)
    seh.push('3rd')
    print(seh)
    seh.push('4th')
    print(seh)
    seh.push('5th')
    print(seh)
    print("Size: {}".format(str(len(seh))))
    print("------------- Popping...") # Pop 2 elements
    seh.pop()
    print(seh)
    print("Size: {}".format(str(len(seh))))
    seh.pop()
    print(seh)
    print("Size: {}".format(str(len(seh))))
    print("------------- Pushing...") # Push in 3 elements
    seh.push('6th')
    print(seh)
    seh.push('7th')
    print(seh)
    seh.push('8th')
    print(seh)
    print("------------- Popping...") # Pop 4 elements
    seh.pop()
    print(seh)
    seh.pop()
    print(seh)
    seh.pop()
    print(seh)
    seh.pop()
    print(seh)
    print("Size: {}".format(str(len(seh))))
    # seh.pop() the empty stack here to test for the IndexError
main()