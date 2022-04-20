# Largely taken from Goodrich et al., Code Fragment 5.3 (p. 196)
# Intended to serve as a simplified version of a python list, to explain how they work

# Jack Micher
# 9/10/2020
# CS/IT 200-03

import ctypes                                       # Provides low-level arrays


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array"""
        self._n = 0                                 # Count actual elements
        self._capacity = 1                          # Default array capacity
        self._A = self._make_array(self._capacity)  # Low-level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if k < -(self._n) or k >= self._n:          # Changed from no negatives to a range -n < k > n
            raise IndexError('Invalid index')
        if k < 0:                                   # Changed to see if k is negative
            return self._A[self._n + k]
        return self._A[k]                           # Retrieve from array
    
    # La# Jack Micher
# 9/3/2020
# CS/IT 200-03b 1 Part 1 implement __setitem__
    def __setitem__(self, k, val):
        """Assign object to pre-existing index of k"""
        if k < 0 or k >= self._n:
            raise IndexError('Invalid index')       # Positive index not found; Index outside of range
        self._A[k] = val

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:               # Not enough room, double capacity
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    # Code Fragment 5.5 (p. 204)
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # For simplicity, assumes that 0 <= k <= n
        if self._n == self._capacity:               # Not enough room, double capacity
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):             # Shift rightmost first, then move left
            self._A[j] = self._A[j-1]
        self._A[k] = value                          # Store newest element
        self._n += 1
    
    # Lab 1 Part 1 implement pop()
    def pop(self):
        """Remove and return last element of the array"""
        if self._n <= 0:                            # Check to see if list is empty
            raise IndexError('No index available; List is empty')
        popped = self._A[self._n - 1]
        self._A[self._n - 1] = None
        self._n -= 1
        if self._n < self._capacity/4:              # If current number of elements is less than C/4...
            self._resize(self._capacity / 2)        # Reduce the capacity by 1/2
        return popped                               # Return the removed element
        
    
    # Code Fragment 5.6 (p. 206)
    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # Does not consider shrinking the array in this version
        for k in range(self._n):
            if self._A[k] == value:                 # Found a match!
                for j in range(k, self._n - 1):     # Shift other elements to fill the gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None         # Fill the old last spot with None
                self._n -= 1                        # Reduce size
                return                              # Exit the function immediately, since we were successful
        raise ValueError('Value not found')

    def _resize(self, c):                           # Non-public utility function
        """Resize internal array to capacity c."""
        B = self._make_array(c)                     # New, bigger array
        for k in range(self._n):                    # For each existing value
            B[k] = self._A[k]
        self._A = B                                 # B is now the array
        self._capacity = c

    def _make_array(self, c):                       # Non-public utility function
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def __str__(self):
        """Return a string represntation of the array."""
        s = '['
        for i in range(self._n):
            if i != 0:
                s += ', '
            s += str(self._A[i])
        s += ']'
        return s
    
    # Lab 1 Part 1 implement __eq__
    def __eq__(self, other):
        if self._n != other._n:
            return False
        for k in range(self._n):
            if self._A[k] != other._A[k]:
                return False
        return True
    
    # Lab 1 Part 2 lab1_v1
    def lab1_v1(self):
        import random
        for x in range(self._n):
            for y in range(x+1, self._n):
                z = random.randint(0, y-x)
                temp = self._A[x]
                self._A[x] = self._A[x+z]
                self._A[x+z] = temp
    
    # Lab 1 Part 2 lab1_v2
    def lab1_v2(self):
        import random
        for i in range(10):
            for j in range(self._n):
                k = random.randint(0,self._n-1)
                temp = self._A[j]
                self._A[j] = self._A[k]
                self._A[k] = temp