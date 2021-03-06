import re
from stack import Stack

def tokenize(exp):
    """Takes in a string expression and tokenizes
    Arguments:
        exp {String} -- string expression
    Return:
        {List} - list of expression
    """
    x = re.split(r'(\d+|\*+|\/+|[a-zA-Z]|[^A-Za-z0-9])', exp)
    return [i for i in x if i.strip()] 

def checkbalance(tokenlist):
    """Checks if there are balances parenthesis
    Arguments:
        tokenlist {List}
    Reuturns:
        {Boolean}
    """
    return tokenlist.count('(') == tokenlist.count(')')

def infixToPostfix(infixexpr):
    """Converts infix expression to postfix expression
    Arguments:
        infixexpr {String}
    Returns:
        postfixexpr {String}
    """
    prec = {
        '**': 4,
        '//': 3,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }
    opStack = Stack()
    postfixList = []
    tokenList = tokenize(infixexpr)
    if not checkbalance(tokenList):
        raise Exception('Unbalanced parenthesis')

    for token in tokenList:
        if bool(re.search(r'(\d+|[A-Z]|[a-z])', token)):
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixExpr):
    """Evaluates postfixexpression
    Arguments:
        postfixExpr {String} -- [description]
    Returns:
        {Float}
    """
    if not isinstance(postfixExpr, str):
        raise TypeError('must pass in string')
    operandStack = Stack()
    tokenList = tokenize(postfixExpr)

    for token in tokenList:
        if bool(re.search(r'(\d+)', token)):
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(op, op1, op2):
    """Evaluates 2 operands with operator in param
    Arguments:
        op {String} -- Operator
        op1 {Integer} -- left operand
        op2 {Integer} -- right operand
    """
    
    if not isinstance(op,str) or \
        not isinstance(op1,int) and not isinstance(op1,float) or\
        not isinstance(op2,int) and not isinstance(op2,float):
        raise TypeError('incorrect op parameter type')
    if not isinstance(op1,int) and not isinstance(op1,float):
        raise TypeError('incorrect op1 parameter type')
    if not isinstance(op2,int) and not isinstance(op2,float):
        raise TypeError('incorrect op2 parameter type')
    dictionary = {
        '**': lambda op1,op2: op1 ** op2,
        '//': lambda op1,op2: op1 // op2,
        '*': lambda op1,op2: op1 * op2,
        '/': lambda op1,op2: op1 / op2,
        '+': lambda op1,op2: op1 + op2,
        '-': lambda op1,op2: op1 - op2
    }
    if op not in dictionary:
        raise ArithmeticError('parameter must be *,/,-,+')
    return dictionary[op](op1, op2)

x = infixToPostfix('A*B+c*d')
print(x)
y = postfixEval('1 2 3 4 5 * + * +')
print(y)