from AExpr import *
from AExprEval import *


x = ImpAExprVal(12)
y = ImpAExprVar('x')
exp1 = ImpAExprBinary(SUM,x,y)
exp2 = ImpAExprBinary(SUB,exp1,exp1)

''' Representamos o estado por um dicionário que mapeia
    identificadores de variáveis em valores inteiros. '''
st = { 'x' : 5 }

# ''' Simplesmente imprimimos as expressões que construimos.'''
# print(x)
# print(y)
# print(exp1)
# print(exp2)

''' Vamos agora criar uma instancia do avaliador'''
ev = AExprEval(st)

''' Vamos avaliar a segunda expressão que criamos anteriormente'''
print('Expressão original:')
print(exp2)
s = ev.eval_one_step(exp2)
print('Primeiro passo')
print(s)
print('Segundo passo')
s1 = ev.eval_one_step(s)
print(s1)
print('Terceiro passo')
s2 = ev.eval_one_step(s1)
print(s2)
print('Quarto passo')
s3 = ev.eval_one_step(s2)
print(s3)
print('Quinto passo')
s4 = ev.eval_one_step(s3)
print(s4)