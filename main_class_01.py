'''Main class for executing'''
from random import randint, random, choice
from copy import deepcopy
from math import log
import tree_01

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


def makerandomtree(pc, maxdepth = 4, fpr = 0.5, ppr = 0.6):
    if random() < fpr and maxdepth > 0:
        f = choice(flist)
        # print(str(f))
        children = [makerandomtree(pc, maxdepth-1, fpr, ppr)
                    for i in range(f.childcount)]
        return tree_01.node(f, children)
    elif random() < ppr:
        return tree_01.paramnode(randint(0, pc-1))
    else:
        return tree_01.constnode(randint(0, 10))


def exampletree():
    return tree_01.node(ifw,[
        tree_01.node(gtw,[tree_01.paramnode(0),tree_01.constnode(3)]),
        tree_01.node(addw,[tree_01.paramnode(1),tree_01.constnode(5)]),
        tree_01.node(subw,[tree_01.paramnode(1),tree_01.constnode(2)]),
                    ]
                )


def hiddenfunction(x, y):
    return x**2+2*y+3*x+5

test_tree = makerandomtree(1)
print (test_tree.evaluate([2, 1]))
# print (test_tree.evaluate([2, 4]))
# print (test_tree.evaluate([5, 3]))
test_tree_02 = makerandomtree(2)
print (test_tree_02.evaluate([5, 3]))
# print (test_tree_02.evaluate([5, 20]))
test_tree.display()
print("-----")
test_tree_02.display()
# exampletree_test = exampletree()
# exampletree_test.evaluate([2, 3])
# exampletree_test.evaluate([5, 3])
# exampletree_test.display()
