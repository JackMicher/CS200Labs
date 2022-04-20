def lab1_v1(self):
    import random
    for x in range(self._n):
        for y in range(x+1, self._n):
            z = random.randint(0, y-x)
            temp = self._A[x]
            self._A[x] = self._A[x+z]
            self._A[x+z] = temp
            
def lab1_v2(self):
    import random
    for i in range(10):
        for j in range(self._n):
            k = random.randint(0,self._n-1)
            temp = self._A[j]
            self._A[j] = self._A[k]
            self._A[k] = temp
            
