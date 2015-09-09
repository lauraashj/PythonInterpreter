'''
Created on Nov 10, 2012

@author: Laura
'''
from Statement import Statements

class ifStatements(Statements):
    '''
    classdocs
    '''
    


    def __init__(self, expr, statementList1, statementList2):
        '''
        Constructor
        '''
        self.expr = expr
        self.statementList1= statementList1
        self.statementList2 = statementList2
        
    def getStatement(self):
        if self.expr.getBool():
            self.statementList1.getStatementLists()
        else:
            self.statementList2.getStatementLists()
            