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
    def __self__(self, fw, children):
        self.function = fw.function
        self.name = fw.name
        self.children = children
    def evaluate(self, inp):
        #The var results is initialised to an array of all children nodes for obj inp
        results=[n.evaluate(inp) for n in self.children]
        #Return result of function when array of children is passed to it.
        return self.function(results)
class paramnode:
    def __init__(self, idx):
        self.idx = idx
    def evaluate(self, inp):
        #Return element at index idx in inp array
        return inp[self.idx]
class constnode:
    def __init__(self, v):
        self.v = v
    def evaluate(self, inp):
        return self.v

addw = fwrapper(lambda l:l[0]+l[1], 2, 'add')
subw = fwrapper(lambda l:l[0]-l[1], 2, 'subtract')
mulw = fwrapper(lambda l:l[0]*l[1], 2, 'multiply')

# step 1: We create a function
def iffunc(l):
    if l[0] > 0:
        return l[1]
    else:
        return l[2]

# step 2: We initialise an object fwrapper which takes the function, the number of arguments and the name
ifw = fwrapper(iffunc, 3, 'if')

def isgreater(l):
    if l[0] > l[1]:
        return 1
    else:
        return 0
gtw = fwrapper(isgreater, 2, 'isgreater')

# step 3: We create a new function example, and return a node with the if function as parent
def exampletree():
    #If has 3 arguments, i.e. 3 child nodes which are themselves nodes
    return node(ifw, [
#The first if case we check to see if a value is greater than the constant 3
                        node(gtw, [paramnode(0), constnode(3)]),
#If the above statement is true, then we add 5 to the value
                        node(addw [paramnode(1), constnode(5)]),
#Else we subtract 2 from the value
                        node(subw [paramnode(2, constnode(2))]),
                    ]
                )

flist = [addw, subw, mulw, ifw, gtw]
