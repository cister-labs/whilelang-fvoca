from AExprs import AExpr, AExprEval
from BExpr  import *

""" General Exception for Boolean
        Expressions Evaluation """
class BExprEvalException(Exception):
    pass

""" Evaluation of Boolean expressions """
class BExprEval:

    def __init__(self,state):
        self.__state   = state

    def one_step_val(self,bexp):
        return bexp
        # print("Entering one_step_val")
        # # When it is already a value, just return it
        # if  exp.getType() == BExprCases.BExprVAL:
        #     return exp
        # else:
        #     raise BExprEvalException("Not a value expression")

    # def one_step_var(self,bexp):
    #     print("B: Entering one_step_var")
    #     if exp.getType() == BExprCases.BExprVAR:
    #         # We are not typechecking anything; it is a TODO
    #         if self.__vars[exp.value()] != None:
    #             return BExpr.ImpBExprVal(self.__vars[exp.value()][1])
    #         elif self.__consts[exp.value()] != None:
    #             return BExpr.ImpBExprVal(self.__consts[exp.value()][1])
    #         else:
    #             raise BExprEvalUndefVar(exp.value())
    #     else:
    #         raise BExprEvalException("Not a variable expression")

    def one_step_unary(self,exp):
        print("B: Entering one_step_unary")
        t = exp.inner()
        if isinstance(t,BExprVal):
            return BExprVal(not exp.inner().value())
        elif isinstance(t,BExprUnary):
            return BExprUnary(self.one_step_unary(exp.inner().inner()))
        elif isinstance(t,BExprBinary):
            o = exp.inner().inner_op()
            if o == BExprOps.BExprAND:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprOR,
                    BExpr.ImpBExprUnary(exp.inner().inner_l()),
                    BExpr.ImpBExprUnary(exp.inner().inner_r())
                    )
            elif o == BExprOps.BExprOR:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprAND,
                    BExpr.ImpBExprUnary(exp.inner().inner_l()),
                    BExpr.ImpBExprUnary(exp.inner().inner_r())
                    )
            elif o == BExprOps.BExprEQ:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprNEQ,
                    exp.inner().inner_l(),
                    exp.inner().inner_r()
                )
            elif o == BExprOps.BExprNEQ:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprEQ,
                    exp.inner().inner_l(),
                    exp.inner().inner_r()
                )   
            elif o == BExprOps.BExprAExprGE:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprAExprLT,
                    exp.inner().inner_l(),
                    exp.inner().inner_r()
                )
            elif o == BExprOps.BExprAExprGT:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprAExprLE,
                    exp.inner().inner_l(),
                    exp.inner().inner_r()
                )
            elif o == BExprOps.BExprAExprLE:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprAExprGT,
                    exp.inner().inner_l(),
                    exp.inner().inner_r()
                )
            elif o == BExprOps.BExprAExprLT:
                return BExpr.ImpBExprBinary(
                    BExprOps.BExprAExprGE,
                    exp.inner().inner_l(),
                    exp.inner().inner_r()
                )
            else:
                raise BExprEvalException("Not a binary sub-expression")
        else:
            raise BExprEvalException("Not a unary expression")

    def one_step_binary(self,exp:BExpr.ImpBExprAst):

        # First, check if we are dealing with arithmetic sub-expressions
        if isinstance(exp.inner_l(),AExpr.ImpAExprAst):

            # If left side is fully reduced
            if exp.inner_l().getType() == AExprCases.AExprVAL:

                # If the right side is also reduced
                if exp.inner_r().getType() == AExprCases.AExprVAL:

                    return BExpr.ImpBExprVal(relArithToOp(exp.inner_op())(exp.inner_l(),exp.inner_r()))
                else:

                    f = AExprEval.AExprEval(self.__vars,self.__consts)
                    return BExpr.ImpBExprBinary(exp.inner_op(),exp.inner_l(),f.eval_one_step(exp.inner_r()))
            else:

                f = AExprEval.AExprEval(self.__vars,self.__consts)
                return BExpr.ImpBExprBinary(exp.inner_op(),f.eval_one_step(exp.inner_l()),exp.inner_r())
        else:

            t = exp.inner_l().getType()
            if t == BExprCases.BExprVAL:

                rt = exp.inner_r().getType()
                if rt == BExprCases.BExprVAL:
                    v = relBoolToOp(exp.inner_op())(exp.inner_l().value(),exp.inner_r().value())
                    return BExpr.ImpBExprVal(v)
                elif rt == BExprCases.BExprVAR:
                    return BExpr.ImpBExprBinary(exp.inner_op(),exp.inner_l(),self.one_step_var(exp.inner_r()))
                elif rt == BExprCases.BExprUNARY:
                    x = self.one_step_unary(exp.inner_r())
                    return BExpr.ImpBExprBinary(exp.inner_op(),exp.inner_l(),x)
                else:
                    x = self.one_step_binary(exp.inner_r())
                    return BExpr.ImpBExprBinary(exp.inner_op(),exp.inner_l(),x)
            elif t == BExprCases.BExprVAR:
                x = self.one_step_var(exp.inner_l())
                return BExpr.ImpBExprBinary(exp.inner_op(),x,exp.inner_r())
            elif t == BExprCases.BExprUNARY:
                x = self.one_step_unary(exp.inner_l())
                return BExpr.ImpBExprBinary(exp.inner_op(),x,exp.inner_r())
            else:
                x = self.one_step_binary(exp.inner_l())
                return BExpr.ImpBExprBinary(exp.inner_op(),x,exp.inner_r())

    
    def eval_one_step(self,exp:BExpr.ImpBExprAst):
        t = exp.getType()
        if t == BExprCases.BExprVAL:
            return self.one_step_val(exp)
        elif t == BExprCases.BExprVAR:
            return self.one_step_var(exp)
        elif t == BExprCases.BExprUNARY:
            return self.one_step_unary(exp)
        else:
            return self.one_step_binary(exp)
    
    
    def eval(self,exp:BExpr.ImpBExprAst):
        print(str(exp))
        if  exp.getType() == BExprCases.BExprVAL:
            return exp.value()
        elif exp.getType() == BExprCases.BExprVAR:
            if self.__vars[exp.value()] != None:
                return self.__vars[exp.value()]
            elif self.__consts[exp.value()] != None:
                return self.__consts[exp.value()]
            else:
                raise BExprEvalException
        elif exp.getType() == BExprCases.BExprUNARY:
            e = self.eval(exp.inner())
            return (not e)
        elif exp.getType() == BExprCases.BExprBINARY:
            # Split between ops with arith expressions or not
            if exp.inner_op() in RELATIONAL_OPS_ARITH:
                aeval = AExprEval(self.__vars,self.__consts)
                el = aeval.eval(exp.inner_l())
                er = aeval.eval(exp.inner_r())
                return (relArithToOp(exp.inner_op())(el,er))
            else:
                el = self.eval(exp.inner_l())
                er = self.eval(exp.inner_r())
                return (relBoolToOp(exp.inner_op())(el,er))

