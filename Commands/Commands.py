from colorama import Fore, Style

class ImpStmtException(Exception):
    pass

class Command:
    pass

class Skip(Command):

    def __str__(self):
        return ("["+Fore.RED+"skip"+Style.RESET_ALL+"]")

class Seq(Command):

    def __init__(self,c1,c2):
        self.__head = c1
        self.__tail = c2

    def inner_l(self):
        return self.__head

    def inner_r(self):
        return self.__tail

    def __str__(self):
        return ('[Seq: '+str(self.__head)+"\n"+str(self.__tail))
        
class Assgn(Command):

    def __init__(self,var,exp):
        self.__var = var
        self.__exp = exp

    def name(self):
        return self.__var

    def value(self):
        return self.__exp

    def __str__(self):
        return ('['+Fore.RED+'Assg:\n\t'+Fore.BLUE+self.__var+'\n\t'+Fore.GREEN+str(self.__exp)+Style.RESET_ALL+']')

class IfElse(Command):

    def __init__(self,bexp,lstmt,rstmt):
        self.__cond = bexp
        self.__lstmt = lstmt
        self.__rstmt = rstmt

    def cond(self):
        return self.__cond

    def inner_l(self):
        return self.__lstmt

    def inner_r(self):
        return self.__rstmt

    def __str__(self):
        return ('['+Fore.RED+"If\n\t"+Fore.BLUE+"COND: "+ str(self.__cond) + "\n\t"+Fore.GREEN+"YES: " + str(self.__lstmt) + "\n\t"+Fore.MAGENTA+"NO: " + str(self.__rstmt)+Style.RESET_ALL+"]")

class While(Command):

    def __init__(self,bexp,inv,stmt):
        self.__cond = bexp
        self.__inv  = inv
        self.__stmt = stmt

    def cond(self):
        return self.__cond

    def inv(self):
        return self.__inv

    def inner(self):
        return self.__stmt

    def __str__(self):
        return ("[While <" + str(self.__cond) + "> (" + str(self.__stmt) + ")]")

