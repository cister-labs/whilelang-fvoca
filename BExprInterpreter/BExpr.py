#from .ImpConsts import *

AND = 1
OR  = 2
NOT = 3
AEQ = 4
ALT = 5

def bop2cop(x):
    if x == AND:
        return (lambda a,b : a and b)
    elif x == OR:
        return (lambda a,b : a or b)
    elif x == NOT:
        return (lambda a : not a)
    elif x == AEQ:
        return (lambda a,b : a == b)
    elif x == ALT:
        return (lambda a,b : a < b)
    else:
        raise Exception("Operator not accepted")


class ImpBExprAst(object):
    pass

class ImpBExprAstException(Exception):
    pass

class ImpBExprVal(ImpBExprAst):
    
    def __init__(self,val):
        self.__val = val
        
    def value(self):
        return self.__val

    def __str__(self):
        return "[BExpr Bool: "+str(self.__val)+"]"

class ImpBExprUnary(ImpBExprAst):

    def __init__(self,inner):
        self.__inner = inner
        
    def inner(self):
        return self.__inner

    def __str__(self):
        return ('[BExpr Unary' + str(self.__inner) + ']')

class ImpBExprBinary(ImpBExprAst):

    def __init__(self,op,lnode,rnode):
        self.__lnode = lnode
        self.__rnode = rnode
        self.__op = op
        
    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def inner_op(self):
        return self.__op

    def __str__(self):
        return ('[BExpr Binary: ' + str(self.__lnode) + ' ' + str(self.__op) + ' ' + str(self.__rnode) + ']')        