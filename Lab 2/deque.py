# Jack Micher
# 9/17/2020
# CS/IT 200-03


class Deque:
    
    class _Node:
        def __init__(self, e, p=None, n=None):
            self._element = e
            self._prev = p
            self._next = n
    
    def __init__(self):
        self.__head = self._Node(e=None)
        self.__tail = self._Node(e=None)
        self.__head._next = self.__tail
        self.__tail._prev = self.__head
        self.__size = 0
    
    def add_to_front(self, item):
        new_node = self._Node(e=item,p=self.__head,n=self.__head._next)
        if self.__size != 0: # If not making a list, make sure that next node links to this new node
            current = self.__head._next
            current._prev = new_node
        self.__head._next = new_node
        if self.__size == 0:
            self.__tail._prev = new_node
        self.__size += 1
    
    def add_to_end(self, item):
        new_node = self._Node(e=item,p=self.__tail._prev,n=self.__tail)
        if self.__size != 0: # If not beginning a list, make sure that prev node links to this new node
            current = self.__tail._prev
            current._next = new_node
        self.__tail._prev = new_node
        if self.__size == 0:
            self.__head._next = new_node
        self.__size += 1
    
    def remove_from_front(self):
        
        
    
    def __str__(self):
        string = '['
        current = self.__head._next
        for i in range(self.__size):
            string += str(current._element)
            current = current._next
            #if current is not None:
            if current != self.__tail:
                string += ', '
        string += ']'
        return string
        