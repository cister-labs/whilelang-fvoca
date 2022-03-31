#from Ast.ImpConsts import AExprCases, AExprOps

''' Constantes que destinguem os tipos de operadores
    para as operações binárias. '''
SUM = 1
SUB = 2
MUL = 3

def aop2cop(x):
    if x == SUM:
        return (lambda a,b : a + b)
    elif x == SUB:
        return (lambda a,b : a - b)
    elif x == MUL:
        return (lambda a,b : a * b)
    else:
        raise Exception("Operator not accepted")



''' Topo da hierarquia de classes. Pura e simplesmente
    determina que todas as subclasses representam um
    tipo específico de expressão aritmética. '''
class ImpAExprAst(object):
    pass

''' Excepção genérica para ser associada a problemas no
    processamento de expressões aritméticas. '''
class ImpAExprAstException(Exception):
    pass

''' Classe que representa uma variável. '''

class ImpAExprVar(ImpAExprAst):

    ''' O construtor recebe como argument uma string que
        representa o identificador da variável. '''    
    def __init__(self,id):
        self.__varId = id

    ''' Acessor ao identificador '''
    def name(self):
        return self.__varId

    ''' Pretty printer para o identificador '''
    def __str__(self):
        return "[Expr Var: " + str(self.__varId) + "]"

''' Classe que representa valores. '''

class ImpAExprVal(ImpAExprAst):
    
    ''' O construtor recebe como argumento um inteiro.'''
    def __init__(self,val):
        self.__val = val

    ''' Acessor ao valor. '''    
    def value(self):
        return self.__val

    ''' Pretty printer para o valor inteiro '''
    def __str__(self):
        return "[Expr Int: " + str(self.__val) + "]"

''' Class que representa operações binárias. '''

class ImpAExprBinary(ImpAExprAst):

    ''' O construtor recebe três argumentos:
        - o operando esquerdo;
        - o operando direito;
        - o operador (que está definido no topo deste ficheiro)'''

    def __init__(self,op,lnode,rnode):
        self.__lnode   = lnode
        self.__rnode   = rnode
        self.__op = op

    ''' Acessor do operando esquerdo. '''
    def inner_l(self):
        return self.__lnode

    ''' Acessor do operando direito. '''
    def inner_r(self):
        return self.__rnode

    ''' O identificador do tipo de operação '''
    def inner_op(self):
        return self.__op

    ''' Pretty printer '''
    def __str__(self):
        def opStr(o):
            if o == SUM:
                return '+'
            elif o == SUB:
                return '-'
            else:
                return '*'
        return ('[Expr Binary: ' + str(self.__lnode) + ' ' + str(opStr(self.__op)) + ' ' + str(self.__rnode) + ']')


