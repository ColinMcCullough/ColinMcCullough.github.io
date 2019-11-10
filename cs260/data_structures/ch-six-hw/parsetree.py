from binarytree import BinaryTree
from cs260.data_structures.ch_three_hw.stack import Stack
import operator
import re

'''
Exercise 1: Extend the build_parse_tree function to handle mathematical expressions that do
not have spaces between every character.
>> Function 'tokenize() acomplishes this

Exercise 2: Modify the build_parse_tree and evaluate functions to handle boolean statements
(and, or, and not). Remember that “not” is a unary operator, so this will complicate your
code somewhat.
'''

def build_parse_tree(fpexp):
    """Builds parse tree, requires fully parenthesized equation
    Arguments:
        fpexp {String} -- Fully parenthesized equation
    Returns:
        eTree {BinaryTree} -- Binary tree build out from Fully parenthesized equation
    """
    fplist = tokenize(fpexp)
    if not checkbalance(fplist):
        raise Exception('Unbalanced parenthesis')
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        #open parenthesis
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        #unary operator
        elif i == 'not':
            parent = pStack.pop()
            currentTree = parent
            currentTree.setRootVal(i)
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        #binary operator
        elif i in ['+', '-', '*','**','//', '/','<','<=','==','!=','>','>=','and','or']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        #close parenthesis
        elif i == ')':
            currentTree = pStack.pop()
        #number or boolean val
        elif i not in ['+', '-', '*', '/', ')']:
            try:
                if(i == 'True' or i == 'False'):
                    currentTree.setRootVal(i)
                else:
                    currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError(f"token {i} is not a valid integer")

    return eTree

def tokenize(exp):
    """Takes in a string expression and tokenizes
    Arguments:
        exp {String} -- string expression
    Return:
        {List} - list of expression
    """
    x = re.split(r'(\d+|\*+|\band|or|<=|==|>=|!=|not\b|\/+|[^A-Za-z0-9])', exp)
    return [i for i in x if i.strip()]

def checkbalance(tokenlist):
    """Checks if there are balances parenthesis
    Arguments:
        tokenlist {List}
    Reuturns:
        {Boolean}
    """
    return tokenlist.count('(') == tokenlist.count(')') 


def postordereval(tree):
    """Evaluates parse tree
    Arguments:
        tree {BinaryTree} -- binary tree built out as parse tree
    """
    opers = get_opers()
    if tree:
        left = postordereval(tree.getLeftChild())
        right = postordereval(tree.getRightChild())
        #two operands
        if left != None and right != None:
            return opers[tree.getRootVal()](left,right)
        #one operand  
        elif left != None and right == None:
            return opers[tree.getRootVal()](left)
        else:
            return tree.getRootVal()

def get_opers():
    return {
    '+':operator.add, 
    '-':operator.sub, 
    '*':operator.mul,
    '**':operator.pow, 
    '/':operator.truediv,
    '//': operator.floordiv,
    '<':operator.lt,
    '<=':operator.le,
    '>':operator.gt,
    '>=':operator.ge,
    '==':operator.eq,
    '!=':operator.ne,
    'and': lambda op1,op2: op1 and op2,
    'or': lambda op1,op2: op1 or op2,
    'not': lambda op1: not op1
    }

def printexp(tree):
    """Builds fully parenthesized string from full parse tree
    Arguments:
        tree {BinaryTree}
    Returns:
        {String}
    """
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal

pt = build_parse_tree('((5 < 6) or (5 > 6))')
print(printexp(pt))
x = postordereval(pt)
print(x)
