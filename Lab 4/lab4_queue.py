import stacks

class Queue:
    def __init__(self):
        self.stackA = stacks.LinkedStack()
        self.stackB = stacks.LinkedStack()
        
    def is_empty(self):
        """Tests if the queue is logically empty"""
        return self.stackA.is_empty()
        
    def enqueue(self, item):
        """Puts item into the back of the queue"""
        self.stackA.push(item)
        
    def first(self):
        """
        Returns the element at the front of the queue, if it exists.
        Raises an IndexError if the queue is empty.
        """
        for i in range(len(self.stackA)):
            self.stackB.push(self.stackA.pop())
        temp = self.stackB.top()
        for i in range(len(self.stackB)):
            self.stackA.push(self.stackB.pop())
        return temp
            
    def dequeue(self):
        """
        Returns and removes the element at the front of the queue, if it exists.
        Raises an IndexError if the queue is empty.
        """
        for i in range(len(self.stackA)):
            self.stackB.push(self.stackA.pop())
        temp = self.stackB.pop()
        for i in range(len(self.stackB)):
            self.stackA.push(self.stackB.pop())
        return temp
        
    def __len__(self):
        """Returns the size of the queue."""
        return len(self.stackA)
    
    def __str__(self):
        return str(self.stackA)

def main():
    testQ = Queue()
    print("Queueing...") # Queue 3 Elements
    testQ.enqueue('1st')
    print(testQ)
    testQ.enqueue('2nd')
    print(testQ)
    testQ.enqueue('3rd')
    print(testQ)
    print("Dequeueing...") # Dequeue 2 Elements
    testQ.dequeue()
    print(testQ)
    testQ.dequeue()
    print(testQ)
    print("Queueing...") # Queue 3 Elements
    testQ.enqueue('4th')
    print(testQ)
    testQ.enqueue('5th')
    print(testQ)
    testQ.enqueue('6th')
    print(testQ)
    print("Dequeueing...") # Dequeue 1 Element
    testQ.dequeue()
    print(testQ)
    print('Current first value: ' + str(testQ.first()))