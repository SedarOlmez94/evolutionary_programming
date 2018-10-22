from random import randint, random, choice
from copy import deepcopy
from math import log

'''Version 1: tree object which includes 4 classes
- fwrapper
- node
- paramnode
- constnode
Date: 01/10/2018'''

class fwrapper:
    def __init__(self, function, childcount, name):
        self.function = function
        self.childcount = childcount
        self.name = name


class node:
    def __init__(self, fw, children):
        self.function = fw.function
        self.name = fw.name
        self.children = children

    def evaluate(self, inp):
        #The var results is initialised to an array of all children nodes for obj inp
        results=[n.evaluate(inp) for n in self.children]
        #Return result of function when array of children is passed to it.
        return self.function(results)

    def display(self, indent=0):
        ''' A recursive display function which first prints the name of the root
            then the children of the roots names.'''
        print(' '*indent+str(self.name))
        for c in self.children:
            c.display(indent+1)

class paramnode:
    def __init__(self, idx):
        self.idx = idx


    def evaluate(self, inp):
        #Return element at index idx in inp array
        return inp[self.idx]


    def display(self, indent=0):
        print('%sp%d' % (' ' * indent, self.idx))


class constnode:
    def __init__(self, v):
        self.v = v


    def evaluate(self, inp):
        return self.v


    def display(self, indent=0):
        print('%s%d' % (' ' * indent, self.v))
