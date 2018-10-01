'''Main class for executing'''
import tree_01
from random import randint, random, choice
from copy import deepcopy
from math import log

# addw = tree_01.fwrapper(lambda l:l[0]+1[1], 2, 'add')
# subw = tree_01.fwrapper(lambda l:l[0]-1[1], 2, 'subtract')
# mulw = tree_01.fwrapper(lambda l:l[0]*1[1], 2, 'multiply')

# # step 1: We create a function
# def iffunc(l):
#     if l[0] > 0:
#         return l[1]
#     else:
#         return l[2]
# # step 2: We initialise an object fwrapper which takes the function, the number of arguments and the name
# ifw = tree_01.fwrapper(iffunc, 3, 'if')
#
# def isgreater(l):
#     if l[0] > l[1]:
#         return 1
#     else:
#         return 0
# gtw = tree_01.fwrapper(isgreater, 2, 'isgreater')


#List of functions
# flist = [addw, subw, mulw, ifw, gtw]

exampletree = tree_01.exampletree
exampletree.evaluate([2, 3])
exampletree.evaluate([5, 3])



# print(exampletree.evaluate([2,3]))
# print(exampletree.evaluate([5, 3]))
