from AExpr import *

''' Função que verifica se o objeto [v] é
    uma instância de um valor; pode ser 
    utilizado como condição de paragem do 
    algoritmo de avaliação. '''
def isFinal(v):
    if isinstance(v,ImpAExprVal):
        return True
    else:
        return False

''' Função para verificar se um determinado objeto é uma
    instância de uma expressão aritmética. '''
def isAExprInstance(o):
    if (isinstance(o,ImpAExprVal) or
        isinstance(o,ImpAExprVar) or
        isinstance(o,ImpAExprBinary)):
        return True
    else:
        return False


""" Evaluation of arithmetic expressions """
class AExprEval:

    ''' O construtor recebe como argumento o estado, ou seja,
        neste caso um dicionário que associa identificadores
        a valores. '''
    def __init__(self,state):
        self._state = state

    ''' A avaliação de um valor retorna o próprio valor. Pode
        ser usado para terminar a avaliação. '''
    def one_step_val(self,exp):
        return exp

    ''' A avaliação de uma variável deve retornar o valor associado.
        Caso o estado não tenha a variável definida, lança uma
        excepção. '''
    def one_step_var(self,exp):
        try:
            return ImpAExprVal(self._state[exp.name()])
        except KeyError as kv:
            raise Exception("Variable not defined in the state.")

    def one_step_binary(self,exp):

        ''' Como a avaliação é feita da direita para a esquerda, primeiro
            temos que perceber que tipo de operando esquerdo temos pela
            frente. '''
        lop = exp.inner_l()

        if isinstance(lop,ImpAExprVal) == False:
            ''' Se o operando esquerdo não é um terminal, i.e., se não é um
            valor, então temos que aplicar a regra que reduz um passo esse
            operando.'''
            if isinstance(lop,ImpAExprVar) :
                return ImpAExprBinary(exp.inner_op(),self.one_step_var(lop),exp.inner_r())
            else:
                x = self.one_step_binary(lop)
                return ImpAExprBinary(exp.inner_op(),x,exp.inner_r())
        else:
            ''' Sabemos agora que o lado esquerdo foi reduzido, portanto podemos
            avançar com a computação do operando direito. '''
            rop = exp.inner_r()

            ''' Se o lado direito também está reduzido, então podemos calcular o
                resultado final. '''
            if isinstance(rop,ImpAExprVal):
                return ImpAExprVal(aop2cop(exp.inner_op())(lop.value(),rop.value()))
            elif isinstance(rop,ImpAExprVar):
                return ImpAExprBinary(exp.inner_op(),lop,self.one_step_var(rop))
            else:
                x = self.one_step_binary(rop)
                return ImpAExprBinary(exp.inner_op(),lop,x)

    ''' Método genérico que avalia qual o tipo de expressão e 
        invoca o método correspondente. '''
    def eval_one_step(self,exp):
        if isinstance(exp,ImpAExprVar):
            print('Evaluating a variable')
            return self.one_step_var(exp)
        elif isinstance(exp,ImpAExprBinary):
            print('Evaluating a binary expression')
            return self.one_step_binary(exp)
        else:
            print('We have a value; nothing to evaluate')
            return exp

# def eval_expr(e,vars,consts):
    
#     res = None

#     if isinstance(e,AExpr.ImpAExprAst):
#         print("Evaluating AExpr")
#         ev = AExprEval(vars,consts)
#         res = ev.eval(e)
#     elif isinstance(e,BExpr.ImpBExprAst):
#         print("Evaluating BExpr")
#         ev = BExprEval(vars,consts)
#         res = ev.eval(e)
#     else:
#         raise AExprEvalGeneric("Unknown type of expression")
#     return res

 #     t = exp.inner_l().getType()
    #     if t == AExprCases.AExprVAL:
    #         print("Left term already reduced; reducing right term!!!")
    #         rt = exp.inner_r().getType()
    #         if rt == AExprCases.AExprVAL:
    #             v = arithToOp(exp.inner_op())(exp.inner_l().value(),exp.inner_r().value())
    #             print(v)
    #             return AExpr.ImpAExprVal(v)
    #         elif rt == AExprCases.AExprVAR:
    #             print(str(t) + str(rt))
    #             return AExpr.ImpAExprBinary(exp.inner_op(),exp.inner_l(),self.one_step_var(exp.inner_r()))
    #         elif rt == AExprCases.AExprUNARY:
    #             print(str(t) + str(rt))
    #             x = self.one_step_unary(exp.inner_r())
    #             return AExpr.ImpAExprBinary(exp.inner_op(),exp.inner_l(),x)
    #         else:
    #             print(str(t) + str(rt))
    #             x = self.one_step_binary(exp.inner_r())
    #             return AExpr.ImpAExprBinary(exp.inner_op(),exp.inner_l(),x)
    #     elif t == AExprCases.AExprVAR:
    #         print("left branch " + str(t))
    #         x = self.one_step_var(exp.inner_l())
    #         return AExpr.ImpAExprBinary(exp.inner_op(),x,exp.inner_r())
    #     elif t == AExprCases.AExprUNARY:
    #         print(str(t))
    #         x = self.one_step_unary(exp.inner_l())
    #         return AExpr.ImpAExprBinary(exp.inner_op(),x,exp.inner_r())
    #     else:
    #         print(str(t))
    #         x = self.one_step_binary(exp.inner_l())
    #         return AExpr.ImpAExprBinary(exp.inner_op(),x,exp.inner_r())
            