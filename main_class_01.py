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
    #A tree with 3 nodes and 4 functions, root is IF statement
    return tree_01.node(ifw,[
        tree_01.node(gtw,[tree_01.paramnode(0),tree_01.constnode(3)]),
        tree_01.node(addw,[tree_01.paramnode(1),tree_01.constnode(5)]),
        tree_01.node(subw,[tree_01.paramnode(1),tree_01.constnode(2)]),
                    ]
                )


def hiddenfunction(x, y):
    return x**2+2*y+3*x+5


def buildhiddenset():
    rows = [] #Empty list
    for i in range(200):
        x = randint(0, 40) #x is a random integer between 0 and 40
         #200 iterations
        y = randint(0, 40) #y is a random integer between 0 and 40
        rows.append([x, y, hiddenfunction(x, y)])
    return rows


def scorefunction(tree, s):
    dif = 0
    for data in buildhiddenset():
        v = tree.evaluate([data[0], data[1]])
        dif += abs(v - data[2])
    return dif

'''We check to see if the root is to be mutated, if not then we traverse
    to the children nodes and try again. Either: a node will be mutated, no node
    will be mutated from top to bottom or some nodes will be mutated. this
    all depends on the random() functions output.'''
def mutate(t, pc, probchange=0.1):
    if random() < probchange:
        return makerandomtree(pc)
    else:
        result = deepcopy(t)
        if isinstance(t, tree_01.node):
            result.children = [mutate(c, pc, probchange) for c in t.children]
        return result


test_tree = makerandomtree(1)
print (test_tree.evaluate([2, 1]))
# test_tree_02 = makerandomtree(2)
# print (test_tree_02.evaluate([5, 3]))
test_tree.display()
# test_tree_02.display()
mutation_tree_01 = mutate(test_tree, 2)
print("---")
print(mutation_tree_01.display())

# Note: if our scorefunction returns 0 then our program is absolutely correct, this is an extremely rare outcome.
print("Result for test_tree_01: " + str(scorefunction(test_tree, buildhiddenset())))
print("Result for mutation_tree_01: " + str(scorefunction(mutation_tree_01, buildhiddenset())))
# print("Result for test_tree_02: " + str(scorefunction(test_tree_02, buildhiddenset())))
