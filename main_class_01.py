'''Main class for executing'''
import tree_01
from random import randint, random, choice
from copy import deepcopy
from math import log

addw = tree_01.fwrapper(lambda l:l[0]+l[1],2,'add')
subw = tree_01.fwrapper(lambda l: l[0] - l[1], 2, 'subtract')
mulw = tree_01.fwrapper(lambda l:l[0]*l[1],2,'multiply')


def iffunc(l):
    if l[0]>0:
        return l[1]
    else:
        return l[2]


ifw = tree_01.fwrapper(iffunc, 3, 'if')
def isgreater(l):
    if l[0]>l[1]:
        return 1
    else:
        return 0


gtw = tree_01.fwrapper(isgreater, 2, 'isgreater')
flist=[addw, mulw, ifw, gtw, subw]

def exampletree():
    return tree_01.node(ifw,[
        tree_01.node(gtw,[tree_01.paramnode(0),tree_01.constnode(3)]),
        tree_01.node(addw,[tree_01.paramnode(1),tree_01.constnode(5)]),
        tree_01.node(subw,[tree_01.paramnode(1),tree_01.constnode(2)]),
                    ]
                )

exampletree_test = exampletree()
print (exampletree_test.evaluate([2, 3]))
print (exampletree_test.evaluate([5, 3]))