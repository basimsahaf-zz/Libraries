"""Arrays in Python are in-built dynamic arrays. I made this module to understand
how arrays work in Python."""


import ctypes


class DynamicArray(object):


    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)


    #returns the length of the dynamic array
    def __len__(self):
        return self.n

    #returns an item at index k, if k is in bounds
    def __getitem__(self,k):

        if not 0 <= k < self.n:
            return IndexError('k is out of bounds')

        return self.A[k]

    #appends an element at the end of the array
    def append(self,element):

        if self.n == self.capacity:
            self._resize(self.capacity*2)  # 2x if capacity isn't enough

        self.A[self.n]=element
        self.n +=1

    #uses the technique of amortization to increase array size
    def _resize(self,new_capacity):

        #make a new array
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity


    #makes a new array with size- new_cap
    def make_array(self,new_cap):

        return (new_cap * ctypes.py_object)()
