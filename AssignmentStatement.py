'''
Created on Nov 10, 2012

@author: Laura
'''
from Statement import Statements
from Memory import MemoryS

class AssignmentStatements(Statements):
    '''
    classdocs
    '''


    def __init__(self, var, expr):
        '''
        Constructor
        '''
        self.var = var
        self.expr = expr
        
        
    def getStatement(self):        
        MemoryS.store(self, self.var.getChar(), self.expr.getExpression())
        
        # self should not be an argument
        
        #self.var.MemoryS.store(self.expr.getExpression())
        
        