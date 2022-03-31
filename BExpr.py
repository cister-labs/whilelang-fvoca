from .ImpConsts import *

class ImpBExprAst(object):

    def __init__(self,ty):
        self.__bexprType = ty

    def getType(self):
        return self.__bexprType

class ImpBExprAstException(Exception):
    pass

class ImpBExprVar(ImpBExprAst):

    def __init__(self,id):
        super().__init__(BExprCases.BExprVAR)
        self.__varId = id
    
    def value(self):
        return str(self.__varId)
        
    def __str__(self):
        return "[BExp Var: "+str(self.__varId)+"]"

class ImpBExprVal(ImpBExprAst):
    
    def __init__(self,val):
        super().__init__(BExprCases.BExprVAL)
        self.__val = val
        
    def value(self):
        return self.__val

    def __str__(self):
        return "[BExpr Bool: "+str(self.__val)+"]"

class ImpBExprUnary(ImpBExprAst):

    def __init__(self,inner):
        super().__init__(BExprCases.BExprUNARY)
        self.__inner = inner
        
    def inner(self):
        return self.__inner

    def __str__(self):
        return ('[BExpr Unary' + str(self.__inner) + ']')

class ImpBExprBinary(ImpBExprAst):

    def __init__(self,op,lnode,rnode):
        super().__init__(BExprCases.BExprBINARY)
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