from AExprs import *

''' Constantes que identificam as operações Booleanas
    previstas para a linguagem de expressões lógicas. '''
AND = 4
OR  = 5
NOT = 6
AEQ = 7
ALT = 8

''' Função de ordem superior que retorna funções que 
    concretizam operadores lógicos abstratos'''
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


class BExpr(object):
    pass

class BExprException(Exception):
    pass

class BExprVal(BExpr):
    
    def __init__(self,val):
        self.__val = val
        
    def value(self):
        return self.__val

    def __str__(self):
        return "[BExpr Bool: "+str(self.__val)+"]"

class BExprUnary(BExpr):

    def __init__(self,inner):
        self.__inner = inner
        
    def inner(self):
        return self.__inner

    def __str__(self):
        return ('[BExpr Unary' + str(self.__inner) + ']')

class BExprBinary(BExpr):

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